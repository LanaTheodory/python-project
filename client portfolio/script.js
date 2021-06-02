let chatBoxPerview = document.querySelector(".perview-box-msg");
let msgBoxSend = document.querySelector("#msgBoxSend");
let msgBtnSend = document.querySelector("#sendMsg");

function sendMessage() {
  const msgValue = msgBoxSend.value;
  if (msgValue.trim().length == 0) return false;

  const newMsg = document.createElement("div");
  newMsg.className = "mrm-msg";
  newMsg.innerText = msgValue;
  chatBoxPerview.append(newMsg);
  msgBoxSend.value = "";
  msgBoxSend.focus();
}

msgBtnSend.onclick = sendMessage;
msgBoxSend.onkeyup = (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
};

