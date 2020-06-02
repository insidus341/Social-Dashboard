$(document).ready(function(){
  update_counters_ajax();

  function update_counters_ajax(){
      $.ajax({
        url: "/update",
        success:
          function(data){
           console.log(data)

           if (!data.hasOwnProperty('error'))
           {
               youtube_sub_value = data['youtube_subs']
               youtube_sub_percent = data['youtube_percent']

               twitter_fol_value = data['twitter_followers']
               twitter_fol_percent = data['twitter_percent']

               // Update the circles
               $('#youtube_subscribers').circleProgress('value', youtube_sub_percent);
               $('#youtube_subscribers strong').html(youtube_sub_value)

               $('#twitter_followers').circleProgress('value', twitter_fol_percent);
               $('#twitter_followers strong').html(twitter_fol_value)
           }
        },
        complete: function() {
       // Schedule the next request when the current one's complete
       setInterval(update_counters_ajax, 60000); // The interval set to 60 seconds
     }
    });
  };
})
