$(function() {
    $('#most_user_func_2').click(function(){
        console.log('in most_user_func_2 click event');
        $( '#api-launcher' ).load('/most_user/get_user_info/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#most_user_func_3').click(function(){
        console.log('in most_user_func_3 click event');
        $( '#api-launcher' ).load('/most_user/search/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});

$(function() {
    $('#most_user_func_5').click(function(){
        console.log('in most_user_func_5 click event');
        $( '#api-launcher' ).load('/most_user/deactivate/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});


$(function() {
    $('#most_user_func_6').click(function(){
        console.log('in most_user_func_6 click event');
        $( '#api-launcher' ).load('/most_user/activate/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});
