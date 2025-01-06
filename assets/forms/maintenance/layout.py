from crispy_forms.layout import Layout, Row, Column, Submit

def get_maintenance_layout():
    return Layout(
        Row(
            Column('asset', css_class='md:col-span-2'),
            Column('maintenance_type', css_class='md:col-span-2'),
            css_class='grid grid-cols-1 md:grid-cols-4 gap-4'
        ),
        'description',
        Row(
            Column('maintenance_date', css_class='md:col-span-1'),
            Column('cost', css_class='md:col-span-1'),
            Column('performed_by', css_class='md:col-span-1'),
            css_class='grid grid-cols-1 md:grid-cols-3 gap-4'
        ),
        Row(
            Column('next_maintenance_date', css_class='md:col-span-1'),
            css_class='grid grid-cols-1 md:grid-cols-2 gap-4'
        ),
        'notes',
        Submit('submit', 'Save Maintenance Record', 
               css_class='bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg')
    )