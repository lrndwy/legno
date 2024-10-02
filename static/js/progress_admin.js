(function($) {
    $(document).ready(function() {
        var $tipeField = $('#id_tipe');
        var $proyekField = $('#id_proyek').closest('.form-row');
        var $dokumenField = $('#id_dokumen').closest('.form-row');

        function updateFields() {
            var selectedType = $tipeField.val();
            if (selectedType === 'proyek') {
                $proyekField.show();
                $dokumenField.hide();
            } else if (selectedType === 'dokumen') {
                $proyekField.hide();
                $dokumenField.show();
            } else {
                $proyekField.hide();
                $dokumenField.hide();
            }
        }

        $tipeField.on('change', updateFields);
        updateFields(); // Call on page load
    });
})(django.jQuery);