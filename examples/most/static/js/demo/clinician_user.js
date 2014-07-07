$(function() {
    $('#clinician_user_func_3').click(function(){
        console.log('in clinician_user_func_3 click event');
        $( '#api-launcher' ).load('/clinician_user/search/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#clinician_user_func_4').click(function(){
        console.log('in clinician_user_func_4 click event');
        $( '#api-launcher' ).load('/clinician_user/get_user_info/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#clinician_user_func_5').click(function(){
        console.log('in clinician_user_func_5 click event');
        $( '#api-launcher' ).load('/clinician_user/new/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#clinician_user_func_1').click(function(){
        console.log('in clinician_user_func_1 click event');
        $( '#api-launcher' ).load('/clinician_user/is_provider/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#clinician_user_func_2').click(function(){
        console.log('in clinician_user_func_2 click event');
        $( '#api-launcher' ).load('/clinician_user/set_provider/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});
