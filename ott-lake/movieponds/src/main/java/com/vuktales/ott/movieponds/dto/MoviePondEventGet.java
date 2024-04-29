package com.vuktales.ott.movieponds.dto;

import com.vuktales.ott.movieponds.entity.MoviePond;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class MoviePondEvent {
    private String eventType;
    private MoviePond moviePond;
    private long customerId;
}
