function DetailMovie({id, lg_img, title,rating, runtime, year, description}) {
  return (
    <div key={id}>
      <img src={lg_img} />
      <h3>{title}</h3>
      <span>Raring: {rating}</span>
      <span>Runtime: {runtime}</span>
      <span>Year: {year}</span>
      <div>
        <h4>Description</h4>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default DetailMovie;
