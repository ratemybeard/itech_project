$(document).ready(function() {
//comments class 
	$('.comments').click(function(){
	        var $this = $(this),
			catid = $this.attr("data-catid");
			comid = $('input.chat-input').val();
	         $.get('/rmb/comment_image/', {comment_id: catid, com: comid},
			 function(data){
	     });
	});
//likes class
	$('.likes').click(function(){
		var $this = $(this),
			catid = $this.attr("data-catid");
		$.get('/rmb/like_image/', {like_id: catid}, 
		function (data) {
			$this.html(data).prop('disabled', true);
		});
	});
//dislikes class
	$('.dislikes').click(function(){
        var $this = $(this), 
			catid = $(this).attr("data-catid2");
	    $.get('/rmb/dislike_image/', {dislike_id: catid}, 
		function(data){
			$this.html(data).prop('disabled',true);
	    });
	    });
});