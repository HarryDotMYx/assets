document.addEventListener('DOMContentLoaded', function() {
    const assetTypeSelect = document.querySelector('[name="asset_type"]');
    const manufacturerSelect = document.querySelector('[name="manufacturer"]');

    const manufacturers = {
        laptop: [
            ['Dell', 'Dell'],
            ['HP', 'HP'],
            ['Lenovo', 'Lenovo'],
            ['Apple', 'Apple'],
            ['Asus', 'Asus'],
            ['Acer', 'Acer'],
            ['Microsoft', 'Microsoft'],
            ['MSI', 'MSI'],
            ['Razer', 'Razer'],
            ['Samsung', 'Samsung']
        ],
        server: [
            ['Dell', 'Dell (PowerEdge)'],
            ['HPE', 'HPE (ProLiant)'],
            ['Lenovo', 'Lenovo (ThinkSystem)'],
            ['IBM', 'IBM'],
            ['Cisco', 'Cisco'],
            ['Supermicro', 'Supermicro'],
            ['Huawei', 'Huawei'],
            ['Oracle', 'Oracle'],
            ['Fujitsu', 'Fujitsu'],
            ['Inspur', 'Inspur']
        ],
        desktop: [
            ['Dell', 'Dell'],
            ['HP', 'HP'],
            ['Lenovo', 'Lenovo'],
            ['Acer', 'Acer'],
            ['Asus', 'Asus'],
            ['Apple', 'Apple (iMac)'],
            ['MSI', 'MSI'],
            ['CyberPowerPC', 'CyberPowerPC'],
            ['Origin', 'Origin PC'],
            ['iBUYPOWER', 'iBUYPOWER']
        ],
        network: [
            ['Cisco', 'Cisco Systems'],
            ['Ubiquiti', 'Ubiquiti'],
            ['Netgear', 'Netgear'],
            ['Aruba', 'Aruba Networks'],
            ['MikroTik', 'MikroTik'],
            ['Juniper', 'Juniper Networks'],
            ['TP-Link', 'TP-Link'],
            ['Huawei', 'Huawei'],
            ['HPE', 'HPE (Aruba)'],
            ['Fortinet', 'Fortinet']
        ],
        other: [
            ['Logitech', 'Logitech (peripherals)'],
            ['Razer', 'Razer (gaming peripherals)'],
            ['APC', 'APC (power equipment)'],
            ['Eaton', 'Eaton (UPS systems)'],
            ['Synology', 'Synology (NAS)'],
            ['QNAP', 'QNAP (NAS)'],
            ['Seagate', 'Seagate (storage)'],
            ['WD', 'Western Digital'],
            ['Sony', 'Sony'],
            ['Panasonic', 'Panasonic']
        ]
    };

    function updateManufacturerOptions(assetType) {
        if (!manufacturerSelect) return;
        
        const options = manufacturers[assetType] || manufacturers.other;
        const currentManufacturer = manufacturerSelect.getAttribute('data-current-value');
        
        manufacturerSelect.innerHTML = '<option value="">Select Manufacturer</option>';
        
        options.forEach(([value, label]) => {
            const option = new Option(label, value);
            if (value === currentManufacturer) {
                option.selected = true;
            }
            manufacturerSelect.add(option);
        });
    }

    if (assetTypeSelect && manufacturerSelect) {
        // Store the current manufacturer value
        const currentManufacturer = manufacturerSelect.value;
        manufacturerSelect.setAttribute('data-current-value', currentManufacturer);
        
        // Initial update
        updateManufacturerOptions(assetTypeSelect.value);
        
        // Update on change
        assetTypeSelect.addEventListener('change', (e) => {
            updateManufacturerOptions(e.target.value);
        });
    }
});