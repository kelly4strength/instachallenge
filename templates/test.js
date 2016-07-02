
 $.ajax({
      type: "GET",
      dataType: "jsonp",
      cache: false,
      url: "https://api.instagram.com/v1/media/popular?access_token=1094228.28feba4.d080c8d8ba0249d6821868edc6808272",
      success: function(data) {
        // placing the images on the page
        }
      }
    });

// $.ajax({
//   type: "GET",
//   dataType: "jsonp",
// 	cache: false,
//   url: "https://api.instagram.com/v1/media/popular?access_token=806401368.5aa13be.4a08df065cbb41469c9cc20041432d3b",
//   success: function(data) {
//     for (var i = 0; i < 6; i++) {
//       $(".popular").append("<li><a target='_blank' href='" + data.data[i].link + "'><img src='" + data.data[i].images.low_resolution.url +"'></img></a></li>");
//     }
//   }
// });

// $.ajax({
//   type: "GET",
//   dataType: "jsonp",
//   url: "https://api.instagram.com/v1/users/25025320/?access_token=806401368.5aa13be.4a08df065cbb41469c9cc20041432d3b",
//   success: function(data) {
//     $('.name').text(data.data.username);
//     $('.tagline').text(data.data.bio);
//   }
// });

// $.ajax({
//   type: "GET",
//   dataType: "jsonp",
//   cache: false,
//   url: "https://api.instagram.com/v1/users/25025320/media/recent/?access_token=806401368.5aa13be.4a08df065cbb41469c9cc20041432d3b",
//   success: function(data) {
//     for (var i = 0; i < 6; i++) {
//     $(".latest").append("<li><a target='_blank' href='" + data.data[i].link +"'><img   src='" + data.data[i].images.low_resolution.url +"'></img></a></li>");
//     }
//   }
// }); 