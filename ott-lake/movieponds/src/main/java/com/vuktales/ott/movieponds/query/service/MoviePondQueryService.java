package com.vuktales.ott.movieponds.query.service;

import com.vuktales.ott.movieponds.dto.MoviePondEvent;
import com.vuktales.ott.movieponds.entity.MoviePond;
import com.vuktales.ott.movieponds.repository.MoviePondRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class MoviePondCommandService {

    @Autowired
    private MoviePondRepository movieprepo;

    @Autowired
    private KafkaTemplate<String, Object> kafkaMoviePondTemplate;

    public MoviePond createMovieRecord(MoviePondEvent movieEvent){
        MoviePond mpObj = movieprepo.save(movieEvent.getMoviePond());
        MoviePondEvent event = new MoviePondEvent(movieEvent.getEventType(), mpObj);
        kafkaMoviePondTemplate.send("movie-record-event-topic",event);
        return mpObj;
    }

    @Transactional(readOnly = false)
    public MoviePond updateMovieRecord(long id, MoviePondEvent movieEvent){
        MoviePond mpExistingObj=null;
        mpExistingObj = movieprepo.getReferenceById(id);

        MoviePond mpNewObj = movieEvent.getMoviePond();
        mpExistingObj.setId(id);
        mpExistingObj.setName(mpNewObj.getName());
        mpExistingObj.setCategory(mpNewObj.getCategory());
        mpExistingObj.setGenere(mpNewObj.getGenere());
        mpExistingObj.setLanguage(mpNewObj.getLanguage());
        mpExistingObj.setReviews(mpNewObj.getReviews());
        mpExistingObj.setImdbRating(mpNewObj.getImdbRating());
        mpExistingObj.setOttSource(mpNewObj.getOttSource());
        mpExistingObj.setSubtitle_language(mpNewObj.getSubtitle_language());
        mpExistingObj.setSuitableAudience(mpNewObj.getSuitableAudience());

        MoviePond mpObj = movieprepo.save(mpExistingObj);
        MoviePondEvent event = new MoviePondEvent(movieEvent.getEventType(), mpObj);
        kafkaMoviePondTemplate.send("movie-record-event-topic",event);
        return mpObj;
    }

    public static void main(String args []){
        MoviePond movieEvent = new MoviePond();
        System.out.println(movieEvent);
    }
}
