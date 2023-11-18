package io.github.vuktales.techbooks.domain;

import jakarta.persistence.*;

import java.util.Objects;
import java.util.Set;

@Entity
public class Pages {

    public Long getId() {
        return Id;
    }

    public void setId(Long id) {
        Id = id;
    }

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long Id;

    public Set<Pages> getPages() {
        return pages;
    }

    public void setPages(Set<Pages> pages) {
        this.pages = pages;
    }

    @ManyToMany(mappedBy = "authors")
    private Set<Pages> pages;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pages pages = (Pages) o;
        return Objects.equals(Id, pages.Id) && Objects.equals(qUrlRef, pages.qUrlRef);
    }

    @Override
    public String toString() {
        return "Pages{" +
                "Id=" + Id +
                ", qUrlRef='" + qUrlRef + '\'' +
                '}';
    }

    @Override
    public int hashCode() {
        return Objects.hash(Id, qUrlRef);
    }

    private String qUrlRef;

}
