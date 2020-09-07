/* code is mostly taken from Emmail.js tutorial and partially from CI's video with some small changed to fit this project */
function sendEmail(contactForm){
    emailjs.send("gmail","watchasellin",{"from_name": contactForm.fname.value + " " + contactForm.lname.value, "from_email": contactForm.email.value, "customer_inquiry": contactForm.message.value})
     .then(function(response) {
       console.log("SUCCESS!", response.status, response.text);
    }, function(error) {
       console.log("FAILED...", error);
    });
    return false;  // To block from loading a new page
}
