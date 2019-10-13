# Recipe Index
tl;dr -- Make our cookbooks' indexes searchable

This is a minimal replica of a multi-user commercial SaaS offering which will allow us to catalog cookbooks we own and
to capture their index pages with a photo, then to upload those pages while associating them with the book. The images
can then have an OCR process run on them, and the resulting text captured in a full text search index. Finally, this
project will include a search function to search that index and yield the cookbooks names and page references for the
search terms. The intent is not to digitize the entire cookbook, and the recipes, but just the indexes.

## Core functionality
This minimal replica is intended as a general exercise in building valuable functionality for humans. For ease of use,
the upload capability will require authentication, but not the search. The functionality will be designed as a single-
tenant solution, meaning it will not allow multiple different people to index their cookbooks separately; it will only
capture one cookbook collection.

## Design considerations
I will use any programming language(s), technologies, tools, and frameworks that I find helpful. This will likely begin
with Python 3 because I am familiar enough with it to get started quickly.

At the start, I expect to design this for deployment within Google Cloud, for reasons.

I am designing this with the intention of it being very cheap to operate. If that doesn't work out as I would expect it
to, I may change strategy with regard to languages, technologies, deployment, or whatever.

## Support
This is very much intended as a personal project so no support should be expected.

## Development process
It will be developed using an [agile methodology](https://modernagile.org) by adding functionality in the smallest
possible increments, and focusing on delivering the greatest value as quickly as possible. When the effort of adding to
this project exceeds the expected payoff I will likely stop work abruptly.

Feature plans are captured in a private Trello board. Issues can be reported on GitHub, and pull requests will be
considered if new automated  tests are included covering the range of possible impacts for the given changes,
documentation is updated as appropriate, and all automated tests pass.

## References
* [Internet Archive :: Open Library Books API](https://openlibrary.org/dev/docs/api/books) for book data
* [GCP :: Cloud Firestore (Datastore Mode)](https://cloud.google.com/firestore/docs/) for book data
* [GCP :: App Engine Search API](https://cloud.google.com/appengine/docs/standard/python/search/) for searching
* [GCP :: Cloud Functions triggered by Cloud Storage](https://cloud.google.com/functions/docs/calling/storage)
