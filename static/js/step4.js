 function timeout() {
     $('.green1').css("animation", "updown 1.2s infinite ease-in-out alternate");
     $('.green2').css("animation", "updown 1.2s 0.2s infinite ease-in-out alternate");
     $('.green3').css("animation", "updown 1.2s 0.4s infinite ease-in-out alternate");
     $('.green4').css("animation", "updown 1.2s 0.6s infinite ease-in-out alternate");
     setTimeout(function() {
         $('.green1').css("animation", "sound-1 1.4s");
         $('.green2').css("animation", "sound-2 1.4s 0.25s");
         $('.yellow').css("animation", "sound-1 1.4s 0.10s");
         $('.green4').css("animation", "sound-2 1.4s 0.15s");
         setTimeout(function() {
             $('.green1').css("animation", "finalani 0.4s");
             $('.green2').css("animation", "finalani 0.4s 0.05s");
             $('.green3').css("animation", "finalani 0.4s 0.1s");
             $('.green4').css("animation", "finalani 0.4s 0.15s");
             setTimeout(function() {
                 timeout();
             }, 550);
         }, 1190);
     }, 3000);
 }

 timeout();


 $("#container").mouseover(function() {
     $('.green1').css("animation", "sound-1 1.4s infinite");
     $('.green2').css("animation", "sound-2 1.4s 0.25s infinite");
     $('.green3').css("animation", "sound-1 1.4s 0.10s infinite");
     $('.green4').css("animation", "sound-2 1.4s 0.15s infinite");
 })