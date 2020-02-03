# Data-science

### Endpoints

The api currently lives at [optimalprice.stromsy.com](optimalprice.stromsy.com).

GET https://optimalprice.stromsy.com/lookup-neighborhood
  * expects URL parameters:
      * longitude: number
      * latitude: number
  * returns JSON object:
  {"neighborhood": neighborhood}
  
POST https://optimalprice.stromsy.com/estimate-price
  * expects form parameters:
      * neighborhood: str
      * room_type: str
      * listings_count: int, total number of listings by the host
      * num_reviews: int, number of reviews on the listing
      * min_nights: int, minimum number of nights on the listing
      * availability: int, number of nights per year the listing is available
      * last_review_time: int, the number of seconds ago that the last review was posted
  * returns JSON object:
  {"price": price}
