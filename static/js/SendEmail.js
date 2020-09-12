/* code is mostly taken from Emmail.js tutorial and partially from CI's video with some small changed to fit this project */
function sendEmail(contactForm){
    emailjs.send("gmail","watchasellin",{"from_name": contactForm.fname.value + " " + contactForm.lname.value, "from_email": contactForm.email.value, "customer_inquiry": contactForm.message.value})
     .then(function(response) {
       console.log("SUCCESS!", response.status, response.text);
       $('#confirmation-msg-success').removeClass("contact-form-msg").addClass("show-contact-form-msg-success");  
       $('.form-control').val('');                
    }, function(error) {
       /*console.log("FAILED...", error);*/
       $('#confirmation-msg-fail').removeClass("contact-form-msg").addClass("show-contact-form-msg-fail");  
       $('.form-control').val('');
    });
    
    
    return false;  // To block from loading a new page
}
