import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom"
import DetailMovie from "../components/DetailMovie";

function Detail() {
  const { id } = useParams();
  const [movieInfo, setMovieIfo] = useState([]);

  const getMovie = async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json();
    setMovieIfo(json.data.movie);
  };
  useEffect(() => {
    getMovie();
  }, []);
//   console.log(movieInfo)
  return (
    <div>
      <h1>Detail</h1>
      <div>
        <DetailMovie id={movieInfo.id} lg_img={movieInfo.large_cover_image} rating={movieInfo.rating} runtime={movieInfo.runtime} year={movieInfo.year} description={movieInfo.description_full} title={movieInfo.title}/>
      </div>

      <button><Link to={'/'}>Back</Link></button>
    </div>
  );
}

export default Detail;
