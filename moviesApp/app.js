const link='http://www.omdbapi.com/?apikey=2e236cf9&t=';

const s1=document.getElementById("intro")
const s2=document.getElementById("loader")
const s3=document.getElementById("error")
const s4=document.getElementById("moviedetails")

s2.classList.add("d-none");
s3.classList.add("d-none");
s4.classList.add("d-none");




const btn=document.getElementById('btn');
const banner=document.getElementById('banner');
const title=document.getElementById('title');
const year=document.getElementById('year');
const genre=document.getElementById('genre');
const plot=document.getElementById('plot');
const director=document.getElementById('director');
const writer=document.getElementById('writer');
const cast=document.getElementById('cast');
const country=document.getElementById('country');
const rating=document.getElementById('rating');
const votes=document.getElementById('votes');
const date=document.getElementById('date');
const time=document.getElementById('time');

function dom(data){
  banner.src=data.Poster;
  title.textContent=data.Title +"  ("+data.Year +")";
  genre.textContent=data.Genre;
  plot.textContent=data.Plot;
  writer.textContent=data.Writer;
  director.textContent=data.Director;
  cast.textContent=data.Actors;
  country.textContent=data.Country;
  rating.textContent=data.imdbRating +" ("+data.imdbVotes+")";
  date.textContent=data.Released;
  time.textContent=data.Runtime;

}

btn.addEventListener('click',()=>{
  let input = document.getElementById('userinput');
  let url=link+input.value;
  input.value="";
                                                          ////////fetching the Data/////////////////////////////////////////////////////////////////////////
  
  fetch(url).then(res=>res.json()).then((data)=>
  {
    s1.classList.add("d-none");
    s2.classList.remove("d-none");
    
    console.log(data);
    if(data["Response"]=="True")
    {
        dom(data);
        s4.classList.remove("d-none")
        s3.classList.add("d-none")
        
    }
      
    
    else{
        s3.classList.remove("d-none")
        s4.classList.add("d-none")
    }

    s2.classList.add("d-none");

  })


})