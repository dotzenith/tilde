# ❖ Jellyfin

Not a ton to say about [Jellyfin](https://jellyfin.org/). Jellyfin will act as the central hub for most of your media.
Just remember to set up the libraries with the proper path during setup.

```plaintext
TV:         /data/tv
Movies:     /data/movies
Music:      /data/music
```

Take a look at the [Jellyfin Docker Compose Template](https://github.com/dotzenith/tilde/blob/main/src/tilde/templates/jellyfin.yml.j2) to understand why that is.
And look at the [Jellyfin Pyinfra Task](https://github.com/dotzenith/tilde/blob/main/src/tilde/tasks/jellyfin.py) to understand where you should put your media for Jellyfin to pick up.
