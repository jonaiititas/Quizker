$(document).ready(function(){
	alert('Hello, world!');
	$("#like_btn").click(function(){
		var quizID
		quizID = $(this).attr('data-quizid');
		
		$.get('/Quizker/like_quiz/',
		      {'quiz_id':quizID},
		      function(data) {
			     $('#like_count').html(data);
			     $('#like_btn').hide();
		})
	});
});


		