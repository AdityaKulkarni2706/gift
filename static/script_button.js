document.getElementById("submit-btn").addEventListener("click", handleSubmit)

async function handleSubmit(event){
    event.preventDefault();
    try{
        const username = document.getElementById("username").value;
        const pwd = document.getElementById("password").value;
        const sendObject = {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({"username":username, "password":pwd})
        }
        console.log(sendObject)

        const response = await fetch("/submit", sendObject);
        const result = await response.json();
        console.log(result["status"]);
        if(result["status"] == "1"){
            console.log("This is 1");
            document.getElementById("display-msg").innerText = "Logged in successfully";
            window.location.href = "/bday";

        }
        else{
            console.log("This is not 1!");
            document.getElementById("display-msg").innerText = "Logged in failed";

        }

    }
    catch{
        console.log("im in catch block");
        document.getElementById("display-msg").innerText = "Your SQLi query is wrong 💀";
    }
}