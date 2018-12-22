var chatLogic = new Vue({
    el: "#chat",
    delimiters: ['{(', ')}'],       //avoid conflicts with django template double brackets

    data: {
        placeholder: 1,
        showChat: false,
        messages: [],
        isInstructor: false,
        isAnonymous: true,
        username: "theres a problem",   //for troubleshooting
        userID: -9999,
        instructorChannel: "notIt"
    },

    methods: {

        setUsername: () => {
            let username = document.getElementById("userName").value
            let instructor = document.getElementById("instructor").checked
            let anonymous = document.getElementById("anonymous").checked
            chatLogic.isInstructor = instructor
            chatLogic.username = username 
            chatLogic.isAnonymous = anonymous
            chatLogic.showChat = true
            let min = 0; 
            let max = 99999999;  
            chatLogic.userID = Math.floor(Math.random() * (+max - +min)) + +min; 
            // userID makes sure that messages will display as your own even when
            // anonymous/ someone else has the same name
            // userID is just a random number and cant be used to 
            // find the identity of a sender to my knowledge
            // there is a possibility of more than one person getting the same ID, but
            // it's very unlikely and if it does happen their messages just show as your own
            // wasn't really a priority for me to fix
            chatLogic.startWebSocket(instructor)
        },

        

        startWebSocket: instructor => {     
            roomName = roomName.replace(/\W/g, '')   
            if(roomName == ""){
                roomName = Math.floor(Math.random() * 9999999)
                roomName = roomName.toString()
            }

            chatLogic.chatSocket = new WebSocket(             
                'ws://' + window.location.host +
                '/ws/chat/' + roomName + '/');    

                chatLogic.chatSocket.onopen = instructor => {   /* make sure messages can only be sent when
                                                                websocket has connected */ 
                    if(instructor){                             // ROW ECHELON FORM 
                        window.setInterval(
                            ()=>{
                                chatLogic.chatSocket.send(JSON.stringify({
                                    'username': chatLogic.username,
                                    'message': "this should be invisible",
                                    'isAnonymous': chatLogic.isAnonymous,
                                    'isInstructor': chatLogic.isInstructor,
                                    'userID': chatLogic.userID,
                                    'invisible': true,
                                }));
                            }, 100)
                        
                    }
                    // The above method constantly sends an invisible message from
                    // the instructor, so everybody in the room will have the correct channel
                    // for sending de-anonymized messages to instructor
                    chatLogic.addListeners()

                }
            
        }, /// End startWebSocket method
        addListeners: () => {
                    document.querySelector('#chat-message-input').onkeyup = event => {
                        if (event.keyCode === 13) {  // enter, return
                            document.querySelector('#chat-message-submit').click();
                        }
                    };
            
                    document.querySelector('#chat-message-submit').onclick = event => {
                        var messageInputDom = document.querySelector('#chat-message-input');
                        var message = messageInputDom.value;
                        /* 
                            standard message send method, anonymity logic is handled server
                            side to avoid revealing anonymous names to people with basic web
                            programming knowledge. 
                    
                        */
                        chatLogic.chatSocket.send(JSON.stringify({
                            'username': chatLogic.username,
                            'message': message,
                            'isAnonymous': chatLogic.isAnonymous,
                            'isInstructor': chatLogic.isInstructor,
                            'userID': chatLogic.userID,
                            'instructorChannel': chatLogic.instructorChannel,
                            'invisible': false,
                        }));
                        messageInputDom.value = '';
                    };

                

            chatLogic.chatSocket.onmessage = (e) => {
                var data = JSON.parse(e.data);
                

                let messageObject = {
                    anonymous: data['anonymous'],
                    username: data['username'] + ": ",
                    message: data['message'],
                    isMine: data['userID'] == chatLogic.userID,
                    invisible: data['invisible'],
                    forInstructor: data['forInstructor'],
                }

                if(data['message'] == "XXX"){
                    console.log(data)
                }

                if(messageObject.isMine){
                    messageObject.username = ""
                }

                if(data.instructorChannel){
                    chatLogic.instructorChannel = data.instructorChannel
                }
                chatLogic.addMessage(messageObject)

                
          
            };

            chatLogic.chatSocket.onclose = e => {
                console.error('Chat socket closed unexpectedly');
            };

            document.querySelector('#chat-message-input').focus();
            

        }, //end addlisteners
        addMessage: (message) => {      
            if(!message.invisible){ //Disregards the constant instructor messages
                    if(message.forInstructor && chatLogic.isInstructor){
                        chatLogic.messages.push(message)
                    }
                    else if(!chatLogic.isInstructor){
                        chatLogic.messages.push(message)
                    }
                }        
            
        },    //End addMessage method
    },


    

})