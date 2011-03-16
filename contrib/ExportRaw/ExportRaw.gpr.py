register(EXPORT,
         id    = 'Raw Export',
         name  = _('Raw Export'),
         description =  _('This is a raw python object dump'),
         version = '1.0.3',
         gramps_target_version = '3.3',
         status = STABLE,
         fname = 'ExportRaw.py',
         export_function = 'exportData',
         export_options = 'WriterOptionBox',
         export_options_title = _('Raw options'),
         extension = "raw"
         )
