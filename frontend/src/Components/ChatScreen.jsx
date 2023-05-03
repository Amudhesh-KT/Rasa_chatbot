import React, { useState, useRef, useEffect } from "react";
import "./ChatScreen.css";
import DigiverzLogo from "./Digiverz-logo.png";
import DigiverzLogoDark from "./Digiverz-logo-dark.png";
import DigiverzMenu from "./chatBotGif.gif";
import darkModeIcon from "./dark-mode.png";
import lightModeIcon from "./light-mode.png";
import darkMode from "./dark-mode.png";
// import ExternalLink from "./external-link.svg";
// import ExternalLinkDark from "./external-link-dark.svg";
import ExternalLink from "./link-light.svg";
import ExternalLinkDark from "./link-dark.svg";
import send from "./send.png";
import sendDark from "./send-dark.png";
import UserIcon from "./user.png";
import UserIconDark from "./user-dark.png";
import ChatBotIcon from "./chatbot.png";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

const Home = () => {
  const [chat, setChat] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [botTyping, setBotTyping] = useState(false);
  const [userTyping, setUserTyping] = useState(false);
  const [chatIDCounter, setChatIDCounter] = useState(1);
  const [darkMode, setDarkMode] = useState(false);
  const [viewMoreState, setViewMoreState] = useState({
    id: 0,
    count: 10,
  });
  const chatScreenContent = useRef();
  useEffect(() => {
    chatScreenContent.current.scrollTop =
      chatScreenContent.current.scrollHeight;
  }, [chat]);

  useEffect(() => {
    if (inputMessage != "") setUserTyping(true);
    else setUserTyping(false);
  }, [inputMessage]);

  const handleSubmit = (evt) => {
    evt.preventDefault();
    if (inputMessage == "") return;

    const name = "shreyas";
    const request_temp = {
      sender: "user",
      sender_id: name,
      msg: inputMessage,
      chat_id: chatIDCounter,
      actions: [],
      links: [],
      details: {},
    };

    setChat((chat) => [...chat, request_temp]);
    setChatIDCounter(chatIDCounter + 1);
    setBotTyping(true);
    setInputMessage("");
    rasaAPI(name, inputMessage);
  };
  const handleButtonRequest = (actionValue) => {
    setUserTyping(false);

    const name = "diwa";
    const request_temp = {
      sender: "user",
      sender_id: name,
      chat_id: chatIDCounter,
      msg: actionValue,
      actions: [],
      links: [],
      details: {},
    };

    setChat((chat) => [...chat, request_temp]);
    setChatIDCounter(chatIDCounter + 1);
    setBotTyping(true);
    rasaAPI(name, actionValue);
  };

  const rasaAPI = async function handleClick(name, msg) {
    await fetch("http://localhost:5005/webhooks/rest/webhook", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        charset: "UTF-8",
      },
      credentials: "same-origin",
      body: JSON.stringify({ sender: name, message: msg }),
    })
      .then((response) => response.json())
      .then((response) => {
        if (response) {
          console.log(response[0]);
          const temp = response[0];
          const recipient_id = "";
          let recipient_msg;
          let response_temp;
          try {
            recipient_msg = JSON.parse(temp["text"]);
            response_temp = {
              sender: "bot",
              recipient_id: recipient_id,
              msg: recipient_msg["msg"],
              actions: recipient_msg["requests"]
                ? recipient_msg["requests"]
                : [],
              links: recipient_msg["links"] ? recipient_msg["links"] : [],
              details: recipient_msg["details"] ? recipient_msg["details"] : {},
            };
          } catch {
            recipient_msg = temp["text"];
            response_temp = {
              sender: "bot",
              recipient_id: recipient_id,
              msg: recipient_msg,
              chat_id: chatIDCounter,
              actions: [],
              links: [],
              details: {},
            };
          }
          setBotTyping(false);
          setUserTyping(false);
          console.log(chat);
          setChat((chat) => [...chat, response_temp]);
          setChatIDCounter(chatIDCounter + 1);
          // scrollBottom();
        }
      });
  };

  return (
    <div
      style={{
        textAlign: "center",
        position: "relative",
        width: "100%",
        height: "100vh",
        backgroundColor: darkMode ? "#31314f" : "white",
      }}
    >
      <div className="chatscreen-container">
        <div
          className="chatscreen-header"
          style={{
            background: darkMode ? "#12111B" : "white",
          }}
        >
          <div className="chatscreen-header-logo">
            <img src={darkMode ? DigiverzLogoDark : DigiverzLogo} alt="Logo" />
          </div>
          {/* <div className="chatscreen-header-menu">
          <img src={DigiverzMenu} alt="Logo" />
        </div> */}
          <div className="chatscreen-header-mode">
            <img
              src={darkMode ? lightModeIcon : darkModeIcon}
              alt="Logo"
              onClick={() => setDarkMode(!darkMode)}
            />
          </div>
        </div>
        <div
          className="chatscreen-content"
          ref={chatScreenContent}
          style={{
            background: darkMode ? "#151826" : "",
          }}
        >
          {chat.map((chatContent, index) => {
            return (
              <div
                key={index}
                style={{
                  justifyContent:
                    chatContent.sender == "bot" ? "flex-start" : "flex-end",
                }}
                className="chartscreen-content-text"
              >
                {chatContent.sender == "bot" ? (
                  <span className="chatscreen-content-icon">
                    <img src={ChatBotIcon} />
                  </span>
                ) : (
                  <></>
                )}
                {/* Chat Contents */}
                <div
                  className="chatscreen-content-chat"
                  style={{
                    alignItems:
                      chatContent.sender == "bot" ? "flex-start" : "flex-end",
                  }}
                >
                  {chatContent.msg ? (
                    <span
                      className="chatscreen-content-msg"
                      style={{
                        borderTopLeftRadius:
                          chatContent.sender == "bot" ? "0px" : "",
                        borderTopRightRadius:
                          chatContent.sender == "user" ? "0px" : "",
                        background: darkMode ? "#4D38A2" : "#2c3880",
                      }}
                    >
                      {chatContent.msg}
                    </span>
                  ) : (
                    <></>
                  )}

                  {chatContent.links ? (
                    <div className="chatscreen-content-links">
                      {chatContent.links.map((link, linkIndex) => (
                        <a
                          href={link.link}
                          target="_blank"
                          style={{
                            color: darkMode ? "white" : "",
                            gridColumn:
                              chatContent.links.length < 6 ? "span 2" : "",
                          }}
                        >
                          {link.tag}
                          <img
                            src={darkMode ? ExternalLinkDark : ExternalLink}
                          />
                        </a>
                      ))}
                    </div>
                  ) : (
                    <></>
                  )}

                  {chatContent.actions ? (
                    <div
                      className="chatscreen-content-actions"
                      style={{
                        justifyContent:
                          chatContent.sender == "bot"
                            ? "flex-start"
                            : "flex-end",
                      }}
                    >
                      {chatContent.actions
                        .slice(
                          0,
                          chatContent.chat_id == viewMoreState.id
                            ? viewMoreState.count
                            : 10
                        )
                        .map((action, actionIndex) => (
                          <Button
                            variant={darkMode ? "contained" : "outlined"}
                            key={actionIndex}
                            size="small"
                            sx={{
                              borderColor: darkMode ? "transparent" : "",
                              backgroundColor: darkMode ? "#15357e" : "",
                            }}
                            style={{
                              margin: "5px 10px 5px 0px",
                              textTransform: "capitalize",
                              letterSpacing: "0.4px",
                              fontSize: "10px",
                              fontWeight: "550",
                            }}
                            color="primary"
                            onClick={(e) => {
                              handleButtonRequest(action);
                            }}
                          >
                            {action}
                          </Button>
                        ))}
                      {chatContent.actions.length > 0 ? (
                        <Button
                          variant={darkMode ? "contained" : "outlined"}
                          size="small"
                          style={{
                            margin: "5px 10px 5px 0px",
                            textTransform: "capitalize",
                            letterSpacing: "0.4px",
                            fontSize: "10px",
                            fontWeight: "550",
                          }}
                          sx={{
                            borderColor: darkMode ? "transparent" : "",
                            backgroundColor: darkMode ? "#15357e" : "",
                          }}
                          color="primary"
                          onClick={(e) => {
                            chatContent.chat_id == viewMoreState.id
                              ? setViewMoreState({
                                  ...viewMoreState,
                                  count: viewMoreState.count + 10,
                                })
                              : setViewMoreState({
                                  id: chatContent.chat_id,
                                  count: 20,
                                });
                          }}
                        >
                          View More
                        </Button>
                      ) : (
                        <></>
                      )}
                    </div>
                  ) : (
                    <></>
                  )}
                  {Object.keys(chatContent.details).length > 0 ? (
                    <div
                      className="chatscreen-content-details"
                      style={{
                        background: darkMode
                          ? "rgba(60, 82, 178, 0.20)"
                          : "rgb(11 92 172 / 5%)",
                      }}
                    >
                      {Object.keys(chatContent.details).map(
                        (key, detailsIndex) => (
                          <div>
                            <span
                              style={{
                                color: darkMode ? "white" : "#2a3eb1",
                              }}
                            >
                              {key}
                            </span>
                            <span
                              style={{
                                margin: "0px 4px",
                                color: darkMode ? "lightskyblue" : "",
                              }}
                            >
                              :
                            </span>
                            <span
                              style={{
                                color: darkMode ? "#e5ebff" : "",
                              }}
                            >
                              {chatContent.details[key]}
                            </span>
                          </div>
                        )
                      )}
                    </div>
                  ) : (
                    <></>
                  )}
                </div>
                {/* -------------------- */}
                {chatContent.sender == "user" ? (
                  <span className="chatscreen-content-icon">
                    <img src={darkMode ? UserIconDark : UserIcon} />
                  </span>
                ) : (
                  <></>
                )}
              </div>
            );
          })}
        </div>
        <div
          className="chatscreen-typing-container"
          style={{
            justifyContent: botTyping ? "flex-start" : "flex-end",
            background: darkMode ? "#151826" : "none",
          }}
        >
          {botTyping ? (
            <span
              className="chatscreen-typing-icon"
              style={{
                opacity: userTyping || botTyping ? "1" : "0",
              }}
            >
              <img
                src={ChatBotIcon}
                style={{
                  opacity: botTyping ? "1" : "0",
                }}
              />
            </span>
          ) : (
            <></>
          )}
          <div
            className="chatscreen-typing"
            style={{
              opacity: userTyping || botTyping ? "1" : "0",
            }}
          >
            <span
              className="chatscreen-typing-dots"
              style={{
                background: darkMode ? "white" : "#3b5998",
              }}
            ></span>
            <span
              className="chatscreen-typing-dots"
              style={{
                background: darkMode ? "white" : "#3b5998",
              }}
            ></span>
            <span
              className="chatscreen-typing-dots"
              style={{
                background: darkMode ? "white" : "#3b5998",
              }}
            ></span>
          </div>
          {botTyping ? (
            <></>
          ) : (
            <span className="chatscreen-typing-icon">
              <img
                src={darkMode ? UserIconDark : UserIcon}
                style={{
                  opacity: userTyping ? "1" : "0",
                }}
              />
            </span>
          )}
        </div>
        <div
          className="chatscreen-footer"
          style={{
            background: darkMode ? "#12111B" : "none",
          }}
        >
          <form onSubmit={handleSubmit}>
            <div className="chatscreen-footer-input">
              <TextField
                onChange={(e) => {
                  setInputMessage(e.target.value);
                }}
                id="standard-required"
                disabled={botTyping}
                value={inputMessage}
                variant="standard"
                sx={{
                  ".MuiInput-root": {
                    borderBottom: darkMode ? "1px solid white !important" : "",
                  },
                  input: {
                    color: darkMode ? "white" : "black",
                  },
                }}
                style={{
                  width: "90%",
                }}
              />
            </div>
            <div className="chatscreen-footer-btn">
              <button type="submit" className="chatscreen-send">
                <img src={darkMode ? sendDark : send} />
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Home;
