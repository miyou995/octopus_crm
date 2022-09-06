"use strict";

// Follow function
$('.follow-btn, .following-btn').each(function () {
  var me = $(this),
    follow_text = 'Follow',
    unfollow_text = 'Following';

  me.click(function () {
    if (me.hasClass('following-btn')) {
      me.removeClass('btn-danger');
      me.removeClass('following-btn');
      me.addClass('btn-primary');
      me.html(follow_text);

    } else {
      me.removeClass('btn-primary');
      me.addClass('btn-danger');
      me.addClass('following-btn');
      me.html(unfollow_text);

    }
    return false;
  });
});

 