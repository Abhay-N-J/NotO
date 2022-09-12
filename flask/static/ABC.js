function init()
{
    obj = document.querySelector("select");
    interns = document.querySelectorAll("div")
    interns.forEach((currentvalue) => {
        currentvalue.style.setProperty("display","none")
    })
    interns[0].style.setProperty("display","block")
    obj.addEventListener('click', (e) => {
        interns.forEach((currentvalue) => {
            currentvalue.style.setProperty("display","none")
            })
            interns[0].style.display = "block";
            interns[1].style.display = "block";
            // const name = e.target.
            const name = document.querySelector('select').value;
            objs = document.querySelectorAll("." + name)
            objs.forEach( (currentvalue)=> {
                currentvalue.style.setProperty("display","block")
            });
        });
}