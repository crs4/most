$(function() {
    $('#task_group_func_1').click(function(){
        console.log('in task_group_func_1 click event');
        //$( '#api-launcher-body' ).html($( this ).html());
        $( '#api-launcher' ).load('/task_group/is_provider/', {'caller':$( this ).text()}, function() {
            console.log('loaded');
            $( '#api-launcher' ).modal().show();
        })
    });
});