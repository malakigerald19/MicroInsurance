
(function($) {
    $(function() {
        var selectField = $('#id_usertype'),
            verified = $('#id_underwriter');

        function toggleVerified(value) {
            value == 'U' ? verified.show() : verified.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);


(function($) {
    $(function() {
        var selectField = $('#id_usertype'),
            verified = $('#id_branch');

        function toggleVerified(value) {
            value == 'M' ||  value == 'F' ? verified.show() : verified.hide();
        
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);

(function($) {
    $(function() {
        var selectField = $('#id_usertype'),
            verified = $('#id_name');

        function toggleVerified(value) {
            value == 'M' ||  value == 'F' ? verified.show() : verified.hide();
        
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);

// (function($) {
//     $(function() {
//         var selectField = $('#id_usertype'),
//             verified = $('#id_branch');

//         function toggleVerified(value) {
            
//         }

//         // show/hide on load based on pervious value of selectField
//         toggleVerified(selectField.val());

//         // show/hide on change
//         selectField.change(function() {
//             toggleVerified($(this).val());
//         });
//     });
// })(django.jQuery);