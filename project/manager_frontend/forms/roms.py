# -*- coding: utf-8 -*-
"""
Thread forms for ROM management.
"""
import os
from django.conf import settings
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage

from project.manager_frontend.forms import CrispyFormMixin

# Configure file system storage for ROMs
ROMS_FS_STORAGE = FileSystemStorage(location=settings.RECALBOX_ROMS_PATH, base_url=settings.MEDIA_URL)

class RomDeleteForm(CrispyFormMixin, forms.Form):
    """
    Form to delete multiple ROMs for a specific system.
    """
    form_key = 'delete'
    form_fieldname_trigger = 'delete_submit'
    
    def __init__(self, *args, **kwargs):
        # Pop extra arguments
        self.system = kwargs.pop('system', None)
        self.romchoices = kwargs.pop('romchoices', [])

        # Initialize parent classes
        super().__init__(*args, **kwargs)

        # Define the form field for selecting ROMs
        self.fields['roms'] = forms.MultipleChoiceField(
            choices=self.romchoices,
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label=_("Select ROMs to delete")
        )
    
    def save(self):
        """
        Deletes selected ROM files and returns the list of deleted files.
        """
        roms = self.cleaned_data.get("roms", [])
        deleted_roms = []
        
        for filename in roms:
            system_relative_path = os.path.join(self.system, filename)
            if ROMS_FS_STORAGE.exists(system_relative_path):
                ROMS_FS_STORAGE.delete(system_relative_path)
                deleted_roms.append(system_relative_path)
        
        return deleted_roms


class RomUploadForm(CrispyFormMixin, forms.Form):
    """
    Form to upload a ROM file for a specific system.
    """
    form_key = 'upload'
    form_fieldname_trigger = 'upload_submit'
    
    rom = forms.FileField(
        label=_('ROM file'),
        required=True,
        help_text=_("Upload a valid ROM file for the selected system.")
    )
    
    def __init__(self, *args, **kwargs):
        # Pop extra arguments
        self.system = kwargs.pop('system', None)
        self.system_manifest = kwargs.pop('system_manifest', {})

        # Initialize parent classes
        super().__init__(*args, **kwargs)
    
    def clean_rom(self):
        """
        Validates the uploaded ROM file extension against the system's manifest.
        """
        rom = self.cleaned_data.get('rom')
        if rom:
            # Extract the file extension
            root, ext = os.path.splitext(rom.name)
            ext = ext[1:].lower() if ext.startswith('.') else ext.lower()

            # Validate the extension
            valid_extensions = self.system_manifest.get('extensions', [])
            if valid_extensions and ext not in valid_extensions:
                raise forms.ValidationError(_("Invalid ROM file extension: .{}").format(ext))

        return rom
    
    def save(self):
        """
        Saves the uploaded ROM file and replaces any existing file with the same name.
        """
        rom = self.cleaned_data["rom"]
        system_relative_path = os.path.join(self.system, rom.name)
        
        # Remove the previous file if it exists
        if ROMS_FS_STORAGE.exists(system_relative_path):
            ROMS_FS_STORAGE.delete(system_relative_path)
        
        # Save the new file
        ROMS_FS_STORAGE.save(system_relative_path, rom)
        
        return ROMS_FS_STORAGE.path(system_relative_path)
