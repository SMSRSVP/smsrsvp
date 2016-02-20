// Your accountSid and authToken from twilio.com/user/account
var accountSid = 'ACb4601ebfba5a649c4aae1ccbf6b1ee8f';
var authToken = "a4d6a5026b373ccd8cd7405d8026adfa";
var client = require('twilio')(accountSid, authToken);
 
client.messages.create({
    body: "Jenny please?! I love you <3",
    to: "+16163890356",
    from: "+17038280845"
}, function(err, message) {
    process.stdout.write(message.sid);
});
