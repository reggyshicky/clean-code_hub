const myImage = document.querySelector("img")

myImage.onclick = () => {
    const mySrc = myImage.getAttribute('src');
    if (mySrc === "Images/Image/firefox-icon.png") {
        myImage.setAttribute("src", "Images/Image/firefox2.png");
    }
    else
    {
        myImage.setAttribute("src", "Images/Image/firefox-icon.png");
    }

}

let myButton =  document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName()
{
    const myName = prompt("Please enter your name.");
    if (!myName) {
        setUserName();
    }
    else
    {
        localStorage.setItem("name", myName);
        myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
}
// The setUserName() function contains a prompt() function, which displays a dialog box, similar to alert(). This prompt() 
// function does more than alert(), asking the user to enter data, and storing it in a variable after the user clicks OK. 
// In this case, we are asking the user to enter a name. Next, the code calls on an API localStorage, which allows us to store data 
// in the browser and retrieve it later. We use localStorage's setItem() function to create and store a data item called 'name',
// setting its value to the myName variable which contains the user's entry for the name. Finally, we set the textContent of the 
// heading to a string, plus the user's newly stored name.

if (!localStorage.getItem("name"))
{
    setUserName();
}
else
{
    const storedName = localStorage.getItem("name");
    myHeading.textContent = `Mozilla is cool, ${storedName}`;
}
// This first line of this block uses the negation operator (logical NOT, represented by the !) to check whether the name data exists. If not, 
// the setUserName() function runs to create it. If it exists (that is, the user set a user name during a previous visit), we retrieve the stored 
// name using getItem() and set the textContent of the heading to a string, plus the user's name, as we did inside setUserName().

myButton.onclick = () => {
    setUserName();
};