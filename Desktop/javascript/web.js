function sendMessage() {
    var userInput = document.getElementById("userInput").value;

    // Call Dialogflow API
    $.ajax({
        type: "POST",
        url: "https://api.dialogflow.com/v1/query?v=20150910",
        contentType: "application/json",
        dataType: "json",
        headers: {
            "Authorization": "Bearer YOUR_DIALOGFLOW_ACCESS_TOKEN"
        },
        data: JSON.stringify({
            query: userInput,
            lang: "en",
            sessionId: "somerandomstring"
        }),
        success: function(response) {
            // Handle the response from Dialogflow
            var botResponse = response.result.fulfillment.speech;
            displayMessage(userInput, 'user');
            displayMessage(botResponse, 'bot');
        },
        error: function() {
            // Handle errors
        }
    });
}

function displayMessage(message, sender) {
    var chatbox = document.getElementById("chatbox");
    var messageDiv = document.createElement("div");
    messageDiv.className = sender;
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
}
