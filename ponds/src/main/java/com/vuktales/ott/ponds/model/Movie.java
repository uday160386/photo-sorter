package com.vuktales.ott.ponds.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Data;

@Entity
@Data
public class Movies
{
    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    long id;
    String name;
    String category;
    String genere;
    String ottSource;
    String reviews;
    long peopleWatched;
    String language;
}
