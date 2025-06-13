console.log("hai from js file")
const doc=document.getElementsByTagName("div")
let div=doc[0]
div.textContent="testing"
let pspkDiv=document.getElementById("pspk")
pspkDiv.style.backgroundColor = "yellow"
pspkDiv.style.border="1px solid black"
pspkDiv.textcontent="pspk"
console.log(pspkDiv)
const headings=document.getElementsByTagName("h1")
console.log(headings)
for (let i=0;i<headings.length;i++)
{
    headings[i].style.fontstylr="italic"
}
const allDivs=document.getElementByTagName("div")
for (let i=0;i<alldivs.length;i++)
{
    allDivs[i].style.border="1px solid black"
    allDivs[]
}