(function($) {
    $(document).ready(function() {
        if (document.querySelector('.submit-row')) {
            var printButton = $('<input type="button" value="Cetak" class="default" id="print-button">');
            $('.submit-row').append(printButton);
            
            $('#print-button').click(function() {
                var content = $('.card-body').html();
                var printWindow = window.open('', '_blank');
                printWindow.document.write('<html><head><title>Cetak Proyek</title></head><body>' + content + '</body></html>');
                printWindow.document.close();
                printWindow.print();
            });
        }
    });
})(django.jQuery);
