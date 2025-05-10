---
description: Query the OpenAlex dataset using the magic of The Internet
---

# Quickstart tutorial

Lets use the OpenAlex API to get journal articles and books published by authors at Stanford University. We'll limit our search to articles published between 2010 and 2020. Since OpenAlex is free and openly available, these examples work without any login or account creation. :thumbsup:

{% hint style="info" %}
If you open these examples in a web browser, they will look _much_ better if you have a browser plug-in such as [JSONVue](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) installed.
{% endhint %}

### 1. Find the institution

You can use the [institutions](api-entities/institutions/) endpoint to learn about universities and research centers. OpenAlex has a powerful search feature that searches across 108,000 institutions.

Lets use it to search for Stanford University:

* Find Stanford University\
  [`https://api.openalex.org/institutions?search=stanford`](https://api.openalex.org/institutions?search=stanford)

Our first result looks correct (yeah!):

```json
{
  "id": "https://openalex.org/I97018004",
  "ror": "https://ror.org/00f54p054",
  "display_name": "Stanford University",
  "country_code": "US",
  "type": "education",
  "homepage_url": "http://www.stanford.edu/"
  // other fields removed
}
```

We can use the ID `https://openalex.org/I97018004` in that result to find out more.

### 2. Find articles (works) associated with Stanford University

The [works](api-entities/works/) endpoint contains over 240 million articles, books, and theses :astonished:. We can filter to show works associated with Stanford.

* Show works where at least one author is associated with Stanford University\
  [`https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004`](https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004)

This is just one of the 50+ ways that you can filter works!

### 3. Filter works by publication year

Right now the list shows records for all years. Lets narrow it down to works that were published between 2010 to 2020, and sort from newest to oldest.

* Show works with publication years 2010 to 2020, associated with Stanford University\
  [https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004,publication\_year:2010-2020\&sort=publication\_date:desc](https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004,publication\_year:2010-2020\&sort=publication\_date:desc)

### 4. Group works by publication year to show counts by year

Finally, you can group our result by publication year to get our final result, which is the number of articles produced by Stanford, by year from 2010 to 2020. There are more than 30 ways to group records in OpenAlex, including by publisher, journal, and open access status.

* Group records by publication year\
  [`https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004,publication\_year:2010-2020\&group-by=publication\_year`](https://api.openalex.org/works?filter=institutions.id:https://openalex.org/I97018004,publication\_year:2010-2020\&group-by=publication\_year)

That gives a result like this:

```json
[
  {
    "key": "2020",
    "key_display_name": "2020",
    "count": 18627
  },
  {
    "key": "2019",
    "key_display_name": "2019",
    "count": 15933
  },
  {
    "key": "2017",
    "key_display_name": "2017",
    "count": 14789
  },
  ...
]
```

There you have it! This same technique can be applied to hundreds of questions around scholarly data. The data you received is under a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/), so not only did you access it easily, you can share it freely! :tada:

## What's next?

Jump into an area of OpenAlex that interests you:

* [Works](api-entities/works/)
* [Authors](api-entities/authors/)
* [Sources](api-entities/sources/)
* [Institutions](api-entities/institutions/)
* [Topics](api-entities/topics/)
* [Publishers](api-entities/publishers/)
* [Funders](api-entities/funders/)

And check out our [tutorials](additional-help/tutorials.md) page for some hands-on examples!

# Known issues

OpenAlex is still very new, and so you'll encounter some bugs as you look through the data. This page documents the ones we currently know about.&#x20;

{% hint style="info" %}
&#x20;Please report any other issues you find by emailing us at **support@openalex.org**
{% endhint %}

## Questionable dates

Some dates, notably publication dates, come from external sources like publishers and are included in OpenAlex as-is. Dates in the future can be especially suspect.&#x20;

[https://openalex.org/W4205467938](https://openalex.org/W4205467938) has a publication date of 2023-01-31, for example (if you're reading this after February 2023, that date used to be in the future). This date came from publisher-submitted [Crossref metadata](https://api.crossref.org/v1/works/10.1145/3485132) for this article. Looking at [https://dl.acm.org/doi/10.1145/3485132](https://dl.acm.org/doi/10.1145/3485132), this does seem to be part of an ACM issue-in-progress with a print publication date of 2023-01-31.

[https://openalex.org/W4200151376](https://openalex.org/W4200151376) has a publication date in _2029_. This also comes from the publisher's [Crossref metadata](https://api.crossref.org/v1/works/10.12960/tsh.2020.0006), but it's less plausible that the journal has an issue planned that far in advance. On [https://doi.org/10.12960/tsh.2020.0006](https://doi.org/10.12960/tsh.2020.0006), we see an accepted date of 2019-12-21 and a publication date of 2029-01-31, suggesting that the latter is a typo and the _publication\_date_ is wrong.&#x20;


# API Overview

The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, [add your email](rate-limits-and-authentication.md#the-polite-pool) to all API requests, like `mailto=example@domain.com`.

## Learn more about the API

* [Get single entities](get-single-entities/)
* [Get lists of entities](get-lists-of-entities/) — Learn how to use [paging](get-lists-of-entities/paging.md), [filtering](get-lists-of-entities/filter-entity-lists.md), and [sorting](get-lists-of-entities/sort-entity-lists.md)
* [Get groups of entities](get-groups-of-entities.md) — Group and count entities in different ways
* [Rate limits and authentication](rate-limits-and-authentication.md) — Learn about joining the [polite pool](rate-limits-and-authentication.md#the-polite-pool)
* [Tutorials ](../additional-help/tutorials.md)— Hands-on examples with code

## Client Libraries

There are several third-party libraries you can use to get data from OpenAlex:

* [openalexR](https://github.com/ropensci/openalexR) (R)
* [OpenAlex2Pajek](https://github.com/bavla/OpenAlex/tree/main/OpenAlex2Pajek) (R)
* [KtAlex](https://github.com/benedekh/KtAlex) (Kotlin)
* [PyAlex](https://github.com/J535D165/pyalex) (Python)
* [diophila](https://pypi.org/project/diophila/) (Python)
* [OpenAlexAPI](https://pypi.org/project/openalexapi/) (Python)

If you're looking for a visual interface, you can also check out the free [VOSviewer](https://www.vosviewer.com/), which lets you make network visualizations based on OpenAlex data:

![](<../.gitbook/assets/Screenshot by Dropbox Capture (1).png>)

# Get groups of entities

Sometimes instead of just listing entities, you want to _group them_ into facets, and count how many entities are in each group. For example, maybe you want to count the number of `Works` by [open access status](../api-entities/works/work-object/#open\_access). To do that, you call the entity endpoint, adding the `group_by` parameter. Example:

* Get counts of works by type:\
  [`https://api.openalex.org/works?group_by=type`](https://api.openalex.org/works?group\_by=type)

This returns a `meta` object with details about the query, and a `group_by` object with the groups you've asked for:

```json
{
    meta: {
        count: 246136992,
        db_response_time_ms: 271,
        page: 1,
        per_page: 200,
        groups_count: 15
    },
    group_by: [
        {
            key: "article",
            key_display_name: "article",
            count: 202814957
        },
        {
            key: "book-chapter",
            key_display_name: "book-chapter",
            count: 21250659
        },
        {
            key: "dissertation",
            key_display_name: "dissertation",
            count: 6055973
        },
        {
            key: "book",
            key_display_name: "book",
            count: 5400871
        },
        ...
    ]
}
```

So from this we can see that the majority of works (202,814,957 of them) are type `article`, with another 21,250,659 `book-chapter`, and so forth.

You can group by most of the same properties that you can [filter](get-lists-of-entities/filter-entity-lists.md) by, and you can combine grouping with filtering.

## Group properties

Each group object in the `group_by` list contains three properties:

#### `key`

Value: a string; the [OpenAlex ID](get-single-entities/#the-openalex-id) or raw value of the `group_by` parameter for members of this group. See details on [`key` and `key_display_name`](get-groups-of-entities.md#key-and-key\_display\_name).

#### `key_display_name`

Value: a string; the `display_name` or raw value of the `group_by` parameter for members of this group. See details on [`key` and `key_display_name`](get-groups-of-entities.md#key-and-key\_display\_name).

#### `count`

Value: an integer; the number of entities in the group.

## "Unknown" groups

The "unknown" group is hidden by default. If you want to include this group in the response, add `:include_unknown` after the group-by parameter.

* Group works by [`authorships.countries`](../api-entities/works/work-object/authorship-object.md#countries) (unknown group hidden):\
  [`https://api.openalex.org/works?group_by=authorships.countries`](https://api.openalex.org/works?group\_by=authorships.countries)
* Group works by [`authorships.countries`](../api-entities/works/work-object/authorship-object.md#countries) (includes unknown group):\
  [`https://api.openalex.org/works?group_by=authorships.countries:include_unknown`](https://api.openalex.org/works?group\_by=authorships.countries:include\_unknown)

## `key` and `key_display_name`

If the value being grouped by is an OpenAlex `Entity`, the [`key`](get-groups-of-entities.md#key) and [`key_display_name`](get-groups-of-entities.md#key\_display\_name) properties will be that `Entity`'s `id` and `display_name`, respectively.

* Group `Works` by `Institution`:\
  [`https://api.openalex.org/works?group_by=authorships.institutions.id`](https://api.openalex.org/works?group\_by=authorships.institutions.id)
* For one group, `key` is "[https://openalex.org/I136199984](https://openalex.org/I136199984)" and `key_display_name` is "Harvard University".

Otherwise, `key` is the same as `key_display_name`; both are the raw value of the `group_by` parameter for this group.

* Group `Concepts` by [`level`](../api-entities/concepts/concept-object.md#level):\
  [`https://api.openalex.org/concepts?group_by=level`](https://api.openalex.org/concepts?group\_by=level)
* For one group, both `key` and `key_display_name` are "3".

## Group-by `meta` properties

`meta.count` is the total number of works (this will be all works if no filter is applied). `meta.groups_count` is the count of groups (in the current page).

If there are no groups in the response, `meta.groups_count` is `null`.

Due to a technical limitation, we can only report the number of groups _in the current page,_ and not the total number of groups.

## Paging

The maximum number of groups returned is 200. If you want to get more than 200 groups, you can use cursor pagination. This works the same as it does when getting lists of entities, so [head over to the section on paging through lists of results](get-lists-of-entities/paging.md#cursor-paging) to learn how.

Due to technical constraints, when paging, results are sorted by key, rather than by count.

# Rate limits and authentication

The API is rate-limited. The limits are:

* max 100,000 calls every day, and also
* max 10 requests every second.

If you hit the API more than 100k times in a day or more than 10 in a second, you'll get `429` errors instead of useful data.

Are those rate limits too low for you? No problem! We can raise those limits as high as you need if you subscribe to [our Premium plan](https://openalex.org/pricing). And if you're an academic researcher we can likely do it for free; just drop us a line at [support@openalex.org](mailto:support@openalex.org).

{% hint style="info" %}
Are you scrolling through a list of entities, calling the API for each? You can go way faster by squishing 50 requests into one using our [OR syntax](get-lists-of-entities/filter-entity-lists.md#addition-or). Here's [a tutorial](https://blog.ourresearch.org/fetch-multiple-dois-in-one-openalex-api-request/) showing how.
{% endhint %}

## The polite pool

The OpenAlex API doesn't require authentication. However, it is helpful for us to know who's behind each API call, for two reasons:

* It allows us to get in touch with the user if something's gone wrong--for instance, their script has run amok and we've needed to start blocking or throttling their usage.
* It lets us report back to our funders, which helps us keep the lights on.

Like Crossref (whose approach we are shamelessly stealing), we separate API users into two pools, the polite pool and the common pool. The polite pool has more consistent response times. It's where you want to be.

To get into the polite pool, you just have to give us an email where we can contact you. You can give us this email in one of two ways:

* Add the `mailto=you@example.com` parameter in your API request, like this: [`https://api.openalex.org/works?mailto=you@example.com`](https://api.openalex.org/works?mailto=you@example.com)
* Add `mailto:you@example.com` somewhere in your User-Agent request header.

## Authentication

You don't need an API key to use OpenAlex. However, [premium users](https://help.openalex.org/hc/en-us/articles/24397762024087-Pricing) do get an API key, which grants higher API limits and enables the use of special filters like [`from_updated_date`](../api-entities/works/filter-works.md#from_updated_date). Using the API key is simple; just add it to your URL using the api\_key param.

* Get a list of all works, using the api key 424242:\
  [`https://api.openalex.org/works?api_key=424242`](https://api.openalex.org/works?api_key=424242)



## Usage tips

### Calling the API in your browser

Because the API is all GET requests without fancy authentication, you can view any request in your browser. This is a very useful and pleasant way to explore the API and debug scripts; we use it all the time.

However, this is _much_ nicer if you install an extension to pretty-print the JSON; [JSONVue (Chrome)](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) and [JSONView (Firefox)](https://addons.mozilla.org/en-US/firefox/addon/jsonview) are popular, free choices. Here's what an API response looks like with one of these extensions enabled:

![A lot prettier than cURL](https://i.imgur.com/E7mNLph.png)

---
description: Get a single entity, based on an ID
---

# Get single entities

This is a more detailed guide to single entities in OpenAlex. If you're just getting started, check out [get a single work](../../api-entities/works/get-a-single-work.md).

It's easy to get a singleton entity object from from the API:`/<entity_name>/<entity_id>.` Here's an example:

* Get the work with the [OpenAlex ID](./#the-openalex-id) `W2741809807`: [`https://api.openalex.org/works/W2741809807`](https://api.openalex.org/works/W2741809807)

That will return a [`Work`](../../api-entities/works/work-object/) object, describing everything OpenAlex knows about the work with that ID. You can use IDs other than OpenAlex IDs, and you can also format the IDs in different ways. Read below to learn more.

{% hint style="info" %}
You can make up to 50 of these queries at once by [requesting a list of entities and filtering on IDs using OR syntax](../get-lists-of-entities/filter-entity-lists.md#addition-or).
{% endhint %}

{% hint style="info" %}
To get a single entity, you need a single _unambiguous_ identifier, like an ORCID or an OpenAlex ID. If you've got an ambiguous identifier (like an author's name), you'll want to [search](../get-lists-of-entities/search-entities.md) instead.
{% endhint %}

## The OpenAlex ID

The OpenAlex ID is the primary key for all entities. It's a URL shaped like this: `https://openalex.org/<OpenAlex_key>`. Here's a real-world example:

[`https://openalex.org/W2741809807`](https://openalex.org/W2741809807)

### The OpenAlex Key

The OpenAlex ID has two parts. The first part is the Base; it's always `https://openalex.org/.` The second part is the Key; it's the unique primary key that identifies a given resource in our database.

The key starts with a letter; that letter tells you what kind of entity you've got: **W**(ork), **A**(uthor), **S**(ource), **I**(nstitution), **C**(oncept), **P**(ublisher), or **F**(under). The IDs are not case-sensitive, so `w2741809807` is just as valid as `W2741809807`. So in the example above, the Key is `W2741809807`, and the `W` at the front tells us that this is a `Work`.

Because OpenAlex was launched as a replacement for [Microsoft Academic Graph (MAG)](https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/), OpenAlex IDs are designed to be backwards-compatible with MAG IDs, where they exist. To find the MAG ID, just take the first letter off the front of the unique part of the ID (so in the example above, the MAG ID is `2741809807`). Of course this won't yield anything useful for entities that don't have a MAG ID.

## Merged Entity IDs

At times we need to merge two Entities, effectively deleting one of them. This usually happens when we discover two Entities that represent the same real-world entity - for example, two [`Authors`](../../api-entities/authors/) that are really the same person.

If you request an Entity using its OpenAlex ID, and that Entity has been merged into another Entity, you will be redirected to the Entity it has been merged into. For example, https://openalex.org/A5092938886 has been merged into https://openalex.org/A5006060960, so in the API the former will redirect to the latter:

```bash
$ curl -i https://api.openalex.org/authors/A5092938886
HTTP/1.1 301 MOVED PERMANENTLY
Location: https://api.openalex.org/authors/A5006060960
```

Most clients will handle this transparently; you'll get the data for author A5006060960 without knowing the redirect even happened. If you have stored Entity ID lists and _do_ notice the redirect, you might as well replace the merged-away ID to skip the redirect next time.

## Supported IDs

For each entity type, you can retrieve the entity using by any of the external IDs we support--not just the native OpenAlex IDs. So for example:

* Get the work with this doi: `https://doi.org/10.7717/peerj.4375`:\
  [https://api.openalex.org/works/https://doi.org/10.7717/peerj.4375](https://api.openalex.org/works/https://doi.org/10.7717/peerj.4375)

This works with DOIs, ISSNs, ORCIDs, and lots of other IDs...in fact, you can use any ID listed in an entity's `ids` property, as listed below:

* [`Work.ids`](../../api-entities/works/work-object/#ids)
* [`Author.ids`](../../api-entities/authors/author-object.md#ids)
* [`Source.ids`](../../api-entities/sources/source-object.md#ids)
* [`Institution.ids`](../../api-entities/institutions/institution-object.md#ids)
* [`Concept.ids`](../../api-entities/concepts/concept-object.md#ids)
* [`Publisher.ids`](../../api-entities/publishers/publisher-object.md#ids)

## ID formats

Most of the external IDs OpenAlex supports are canonically expressed as URLs...for example, [the canonical form of a DOI](https://www.crossref.org/display-guidelines/) always starts with `https://doi.org/`. You can always use these URL-style IDs in the entity endpoints. Examples:

* Get the institution with the ROR [https://ror.org/02y3ad647](https://ror.org/02y3ad647) (University of Florida):\
  [`https://api.openalex.org/institutions/https://ror.org/02y3ad647`](https://api.openalex.org/institutions/https://ror.org/02y3ad647)
* Get the author with the ORCID [https://orcid.org/0000-0003-1613-5981](https://orcid.org/0000-0003-1613-5981) (Heather Piwowar):\
  [`https://api.openalex.org/authors/https://orcid.org/0000-0003-1613-5981`](https://api.openalex.org/authors/https://orcid.org/0000-0003-1613-5981)

For simplicity and clarity, you may also want to express those IDs in a simpler, URN-style format, and that's supported as well; you just write the namespace of the ID, followed by the ID itself. Here are the same examples from above, but in the namespace:id format:

* Get the institution with the ROR [https://ror.org/02y3ad647](https://ror.org/02y3ad647) (University of Florida):\
  [`https://api.openalex.org/institutions/ror:02y3ad647`](https://api.openalex.org/institutions/ror:02y3ad647)
* Get the author with the ORCID [https://orcid.org/0000-0003-1613-5981](https://orcid.org/0000-0003-1613-5981) (Heather Piwowar):\
  [`https://api.openalex.org/authors/orcid:0000-0003-1613-5981`](https://api.openalex.org/authors/orcid:0000-0003-1613-5981)

Finally, if you're using an OpenAlex ID, you can be even more succinct, and just use the [Key](./#the-openalex-key) part of the ID all by itself, the part that looks like `w1234567`:

* Get the work with OpenAlex ID https://openalex.org/W2741809807:\
  [https://api.openalex.org/works/W2741809807](https://api.openalex.org/works/W2741809807)

## Canonical External IDs

Every entity has an OpenAlex ID. Most entities also have IDs in other systems, too. There are hundreds of different ID systems, but we've selected a single external ID system for each entity to provide the **Canonical External ID**--this is the ID in the system that's been most fully adopted by the community, and is most frequently used in the wild. We support other external IDs as well, but the canonical ones get a privileged spot in the API and dataset.

These are the Canonical External IDs:

* Works: [DOI](../../api-entities/works/work-object/#title)
* Authors: [ORCID](../../api-entities/authors/author-object.md#orcid)
* Sources: [ISSN-L](../../api-entities/sources/source-object.md#issn\_l)
* Institutions: [ROR ID](../../api-entities/institutions/institution-object.md#ror)
* Concepts: [Wikidata ID](../../api-entities/concepts/concept-object.md#wikidata)
* Publishers: [Wikidata ID](../../api-entities/publishers/publisher-object.md#ids)

## Dehydrated entity objects

The full entity objects can get pretty unwieldy, especially when you're embedding a list of them in another object (for instance, a list of `Concept`s in a `Work`). For these cases, all the entities except `Work`s have a dehydrated version. This is a stripped-down representation of the entity that carries only its most essential properties. These properties are documented individually on their respective entity pages.

\\

# Get lists of entities

It's easy to get a list of entity objects from from the API:`/<entity_name>`. Here's an example:

* Get a list of _all_ the topics in OpenAlex:\
  [`https://api.openalex.org/topics`](https://api.openalex.org/topics)

This query returns a `meta` object with details about the query, a `results` list of [`Topic`](../../api-entities/topics/topic-object.md) objects, and an empty [`group_by`](../get-groups-of-entities.md) list:

```json
meta: {
    count: 4516,
    db_response_time_ms: 81,
    page: 1,
    per_page: 25
    },
results: [
    // long list of Topic entities
 ],
group_by: [] // empty
```

Listing entities is a lot more useful when you add parameters to [page](paging.md), [filter](filter-entity-lists.md), [search](search-entities.md), and [sort](sort-entity-lists.md) them. Keep reading to learn how to do that.

# Autocomplete entities

The autocomplete endpoint lets you add autocomplete or typeahead components to your applications, without the overhead of hosting your own API endpoint.

Each endpoint takes a string, and (very quickly) returns a list of entities that match that string.

Here's an example of an autocomplete component that lets users quickly select an institution:

![A user looking for information on the flagship of Florida's state university system.](https://i.imgur.com/f8yyWCd.png)

This is the query behind that result: [`https://api.openalex.org/autocomplete/institutions?q=flori`](https://api.openalex.org/autocomplete/institutions?q=flori)

The autocomplete endpoint is very fast; queries generally return in around 200ms. If you'd like to see it in action, we're using a slightly-modified version of this endpoint in the OpenAlex website here: [https://explore.openalex.org/](https://explore.openalex.org/)

## Request format

The format for requests is simple: `/autocomplete/<entity_type>?q=<query>`

* `entity_type` (optional): the name of one of the OpenAlex entities: `works`, `authors`, `sources`, `institutions`, `concepts`, `publishers`, or `funders`.
* `query`: the search string supplied by the user.

You can optionally [filter autocomplete results](autocomplete-entities.md#filter-autocomplete-results).

## Response format

Each request returns a response object with two properties:

* `meta`: an object with information about the request, including timing and results count
* `results`: a list of up to ten results for the query, sorted by citation count. Each result represents an entity that matched against the query.

```json
{
    meta: {
        count: 183,
        db_response_time_ms: 5,
        page: 1,
        per_page: 10
    },
    results: [
        {
            id: "https://openalex.org/I33213144",
            display_name: "University of Florida",
            hint: "Gainesville, USA",
            cited_by_count: 17190001,
            entity_type: "institution",
            external_id: "https://ror.org/02y3ad647"
        },
        // more results...
    ]
}
```

Each object in the `results` list includes these properties:

* `id` (string): The [OpenAlex ID](../get-single-entities/#the-openalex-id) for this result entity.
* `external_id` (string): The [Canonical External ID](../get-single-entities/#canonical-external-ids) for this result entity.
* `display_name` (string): The entity's `display_name` property.
* `entity_type` (string): The entity's type: `author`, `concept`, `institution`, `source`, `publisher`, `funder`, or `work`.
* `cited_by_count` (integer): The entity's `cited_by_count` property. For works this is simply the number of incoming citations. For other entities, it's the _sum_ of incoming citations for all the works linked to that entity.
* `works_count` (integer): The number of works associated with the entity. For entity type `work` it's always null.
* `hint`: Some extra information that can help identify the right item. Differs by entity type.

### The `hint` property

Result objects have a `hint` property. You can show this to users to help them identify which item they're selecting. This is particularly helpful when the `display_name` values of different results are the same, as often happens when autocompleting an author entity--a user who types in `John Smi` is going to see a lot of identical-looking results, even though each one is a different person.

The content of the `hint` property varies depending on what kind of entity you're looking up:

* `Work`: The work's authors' display names, concatenated. e.g. "R. Alexander Pyron, John J. Wiens"
* `Author`: The author's [last known institution](../../api-entities/authors/author-object.md#last\_known\_institution), e.g. "University of North Carolina at Chapel Hill, USA"
* `Source`: The `host_organization`, e.g. "Oxford University Press"
* `Institution`: The institution's location, e.g. "Gainesville, USA"
* `Concept`: The Concept's [description](../../api-entities/concepts/concept-object.md#description), e.g. "the study of relation between plant species and genera"

## IDs in autocomplete

[Canonical External IDs](../get-single-entities/#canonical-external-ids) and [OpenAlex IDs](../get-single-entities/#the-openalex-id) are detected within autocomplete queries and matched to the appropriate record if it exists. For example:

* The query [`https://api.openalex.org/autocomplete?q=https://orcid.org/0000-0002-7436-3176`](https://api.openalex.org/autocomplete?q=https://orcid.org/0000-0002-7436-3176) will search for the author with ORCID ID `https://orcid.org/0000-0002-7436-3176` and return 0 records if it does not exist.
* The query [`https://api.openalex.org/autocomplete/sources?q=S49861241`](https://api.openalex.org/autocomplete/sources?q=S49861241) will search for the source with OpenAlex ID `https://openalex.org/S49861241` and return 0 records if it does not exist.

## Filter autocomplete results

All entity [filters](filter-entity-lists.md) and [search](search-entities.md) queries can be added to autocomplete and work as expected, like:

[`https://api.openalex.org/autocomplete/works?filter=publication_year:2010&search=frogs&q=greenhou`](https://api.openalex.org/autocomplete/works?filter=publication\_year:2010\&search=frogs\&q=greenhou)

# Filter entity lists

Filters narrow the list down to just entities that meet a particular condition--specifically, a particular value for a particular attribute.

A list of filters are set using the `filter` parameter, formatted like this: `filter=attribute:value,attribute2:value2`. Examples:

* Get the works whose [type](../../api-entities/works/work-object/#type) is `book`:\
  [`https://api.openalex.org/works?filter=type:book`](https://api.openalex.org/works?filter=type:book)
* Get the authors whose name is Einstein:\
  [`https://api.openalex.org/authors?filter=display_name.search:einstein`](https://api.openalex.org/authors?filter=display\_name.search:einstein)

Filters are case-insensitive.

## Logical expressions

### Inequality

For numerical filters, use the less-than (`<`) and greater-than (`>`) symbols to filter by inequalities. Example:

* Get sources that host more than 1000 works:\
  [`https://api.openalex.org/sources?filter=works_count:>1000`](https://api.openalex.org/sources?filter=works\_count:%3E1000)

Some attributes have special filters that act as syntactic sugar around commonly-expressed inequalities: for example, the `from_publication_date` filter on `works`. See the endpoint-specific documentation below for more information. Example:

* Get all works published between 2022-01-01 and 2022-01-26 (inclusive):\
  [`https://api.openalex.org/works?filter=from_publication_date:2022-01-01,to_publication_date:2022-01-26`](https://api.openalex.org/works?filter=from\_publication\_date:2022-01-01,to\_publication\_date:2022-01-26)

### Negation (NOT)

You can negate any filter, numerical or otherwise, by prepending the exclamation mark symbol (`!`) to the filter value. Example:

* Get all institutions _except_ for ones located in the US:\
  [`https://api.openalex.org/institutions?filter=country_code:!us`](https://api.openalex.org/institutions?filter=country\_code:!us)

### Intersection (AND)

By default, the returned result set includes only records that satisfy _all_ the supplied filters. In other words, filters are combined as an AND query. Example:

* Get all works that have been cited more than once _and_ are free to read:\
  [`https://api.openalex.org/works?filter=cited_by_count:>1,is_oa:true`](https://api.openalex.org/works?filter=cited\_by\_count:%3E1,is\_oa:true)

To create an AND query within a single attribute, you can either repeat a filter, or use the plus symbol (`+`):

* Get all the works that have an author from France _and_ an author from the UK:
  * Using repeating filters: [`https://api.openalex.org/works?filter=institutions.country_code:fr,institutions.country_code:gb`](https://api.openalex.org/works?filter=institutions.country\_code:fr,institutions.country\_code:gb)
  * Using the plus symbol (`+`): [`https://api.openalex.org/works?filter=institutions.country_code:fr+gb`](https://api.openalex.org/works?filter=institutions.country\_code:fr+gb)

Note that the plus symbol (`+`) syntax will not work for search filters, boolean filters, or numeric filters.

### Addition (OR)

Use the pipe symbol (`|`) to input lists of values such that _any_ of the values can be satisfied--in other words, when you separate filter values with a pipe, they'll be combined as an `OR` query. Example:

* Get all the works that have an author from France or an author from the UK:\
  [`https://api.openalex.org/works?filter=institutions.country_code:fr|gb`](https://api.openalex.org/works?filter=institutions.country\_code:fr|gb)

This is particularly useful when you want to retrieve a many records by ID all at once. Instead of making a whole bunch of singleton calls in a loop, you can make one call, like this:

* Get the works with DOI `10.1371/journal.pone.0266781` _or_ with DOI `10.1371/journal.pone.0267149` (note the pipe separator between the two DOIs):\
  [`https://api.openalex.org/works?filter=doi:https://doi.org/10.1371/journal.pone.0266781|https://doi.org/10.1371/journal.pone.0267149`](https://api.openalex.org/works?filter=doi:https://doi.org/10.1371/journal.pone.0266781|https://doi.org/10.1371/journal.pone.0267149)

You can combine up to 100 values for a given filter in this way. You will also need to use the parameter `per-page=100` to get all of the results per query. See our [blog post](https://blog.ourresearch.org/fetch-multiple-dois-in-one-openalex-api-request/) for a tutorial.

{% hint style="danger" %}
You can use OR for values _within_ a given filter, but not _between_ different filters. So this, for example, **doesn't work and will return an error**:

* Get either French works _or_ ones published in the journal with ISSN 0957-1558:\
  [`https://api.openalex.org/works?filter=institutions.country_code:fr|primary_location.source.issn:0957-1558`](https://api.openalex.org/works?filter=institutions.country\_code:fr|primary\_location.source.issn:0957-1558)
{% endhint %}

## Available Filters

The filters for each entity can be found here:

* [Works](../../api-entities/works/filter-works.md)
* [Authors](../../api-entities/authors/filter-authors.md)
* [Sources](../../api-entities/sources/filter-sources.md)
* [Institutions](../../api-entities/institutions/filter-institutions.md)
* [Concepts](../../api-entities/concepts/filter-concepts.md)
* [Publishers](../../api-entities/publishers/filter-publishers.md)
* [Funders](../../api-entities/funders/filter-funders.md)

# Paging

{% hint style="info" %}
You can see executable examples of paging in [this user-contributed Jupyter notebook!](https://github.com/ourresearch/openalex-api-tutorials/blob/main/notebooks/getting-started/paging.ipynb)
{% endhint %}

### Basic paging

Use the `page` query parameter to control which page of results you want (eg `page=1`, `page=2`, etc). By default there are 25 results per page; you can use the `per-page` parameter to change that to any number between 1 and 200.

* Get the 2nd page of a list:\
  [`https://api.openalex.org/works?page=2`](https://api.openalex.org/works?page=2)
* Get 200 results on the second page:\
  [`https://api.openalex.org/works?page=2&per-page=200`](https://api.openalex.org/works?page=2\&per-page=200)

Basic paging only works to get the first 10,000 results of any list. If you want to see more than 10,000 results, you'll need to use [cursor paging](paging.md#cursor-paging).

### Cursor paging

Cursor paging is a bit more complicated than [basic paging](paging.md#basic-paging), but it allows you to access as many records as you like.&#x20;

To use cursor paging, you request a cursor by adding the `cursor=*` parameter-value pair to your query.

* Get a cursor in order to start cursor pagination:\
  [`https://api.openalex.org/works?filter=publication_year:2020&per-page=100&cursor=*`](https://api.openalex.org/works?filter=publication\_year:2020\&per-page=100\&cursor=\*)

The response to your query will include a `next_cursor` value in the response's `meta` object. Here's what it looks like:&#x20;

```json
{
  "meta": {
    "count": 8695857,
    "db_response_time_ms": 28,
    "page": null,
    "per_page": 100,
    "next_cursor": "IlsxNjA5MzcyODAwMDAwLCAnaHR0cHM6Ly9vcGVuYWxleC5vcmcvVzI0ODg0OTk3NjQnXSI="
  },
  "results" : [
    // the first page of results
  ]
}
```

To retrieve the next page of results, copy the `meta.next_cursor` value into the cursor field of your next request.

* Get the next page of results using a cursor value: \
  [`https://api.openalex.org/works?filter=publication_year:2020&per-page=100&cursor=IlsxNjA5MzcyODAwMDAwLCAnaHR0cHM6Ly9vcGVuYWxleC5vcmcvVzI0ODg0OTk3NjQnXSI=`](https://api.openalex.org/works?filter=publication\_year:2020\&per-page=100\&cursor=IlsxNjA5MzcyODAwMDAwLCAnaHR0cHM6Ly9vcGVuYWxleC5vcmcvVzI0ODg0OTk3NjQnXSI=)

This second page of results will have a new value for `meta.next_cursor`. You'll use this new value the same way you did the first, and it'll give you the second page of results. To get _all_ the results, keep repeating this process until `meta.next_cursor` is null and the `results` set is empty.

Besides using cursor paging to get entities, you can also use it in [`group_by` queries](../get-groups-of-entities.md).

{% hint style="danger" %}
**Don't use cursor paging to download the whole dataset.**

* It's bad for you because it will take many days to page through a long list like /works or /authors.
* It's bad for us (and other users!) because it puts a massive load on our servers.

Instead, download everything at once, using the [OpenAlex snapshot](../../download-all-data/openalex-snapshot.md). It's free, easy, fast, and you get all the results in same format you'd get from the API.
{% endhint %}

# Sample entity lists

You can use `sample` to get a random list of up to 10,000 results.

* Get 100 random works\
  [https://api.openalex.org/works?sample=100\&per-page=100](https://api.openalex.org/works?sample=100\&per-page=100)
* Get 50 random works that are open access and published in 2021\
  [https://api.openalex.org/works?filter=open\_access.is\_oa:true,publication\_year:2021\&sample=50\&per-page=50](https://api.openalex.org/works?filter=open\_access.is\_oa:true,publication\_year:2021\&sample=50\&per-page=50)

You can add a `seed` value in order to retrieve the same set of random records, in the same order, multiple times.

* Get 20 random sources with a seed value\
  [https://api.openalex.org/sources?sample=20\&seed=123](https://api.openalex.org/sources?sample=20\&seed=123)

{% hint style="info" %}
Depending on your query, random results with a seed value _may_ change over time due to new records coming into OpenAlex.&#x20;
{% endhint %}

## Limitations

* The sample size is limited to 10,000 results.
* You must provide a `seed` value when paging beyond the first page of results. Without a seed value, you might get duplicate records in your results.
* &#x20;You must use [basic paging](paging.md#basic-paging) when sampling. Cursor pagination is not supported.

# Search entities

## The `search` parameter

The `search` query parameter finds results that match a given text search. Example:

* Get works with search term "dna" in the title, abstract, or fulltext:\
  [`https://api.openalex.org/works?search=dna`](https://api.openalex.org/works?search=dna)

When you [search `works`](../../api-entities/works/search-works.md), the API looks for matches in titles, abstracts, and [fulltext](../../api-entities/works/work-object/README.md#has_fulltext). When you [search `concepts`](../../api-entities/concepts/search-concepts.md), we look in each concept's `display_name` and `description` fields. When you [search `sources`](../../api-entities/sources/search-sources.md), we look at the `display_name`_,_ `alternate_titles`, and `abbreviated_title` fields. When you [search `authors`](../../api-entities/authors/search-authors.md), we look at the `display_name` and `display_name_alternatives` fields. When you [search `institutions`](../../api-entities/institutions/search-institutions.md), we look at the `display_name`, `display_name_alternatives`, and `display_name_acronyms` fields.

For most text search we remove [stop words](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-stop-tokenfilter.html) and use [stemming](https://en.wikipedia.org/wiki/Stemming) (specifically, the [Kstem token filter](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-kstem-tokenfilter.html)) to improve results. So words like "the" and "an" are transparently removed, and a search for "possums" will also return records using the word "possum." With the exception of raw affiliation strings, we do not search within words but rather try to match whole words. So a search with "lun" will not match the word "lunar".

### Search without stemming

To disable stemming and the removal of stop words for searches on titles and abstracts, you can add `.no_stem` to the search filter. So, for example, if you want to search for "surgery" and not get "surgeries" too:

* [`https://api.openalex.org/works?filter=display_name.search.no_stem:surgery`](https://api.openalex.org/works?filter=display_name.search.no_stem:surgery)
* [`https://api.openalex.org/works?filter=title.search.no_stem:surgery`](https://api.openalex.org/works?filter=title.search.no_stem:surgery)
* [`https://api.openalex.org/works?filter=abstract.search.no_stem:surgery`](https://api.openalex.org/works?filter=abstract.search.no_stem:surgery)
* [`https://api.openalex.org/works?filter=title_and_abstract.search.no_stem:surgery`](https://api.openalex.org/works?filter=title_and_abstract.search.no_stem:surgery)

### Boolean searches

Including any of the words `AND`, `OR`, or `NOT` in any of your searches will enable boolean search. Those words must be UPPERCASE. You can use this in all searches, including using the `search` parameter, and using [search filters](search-entities.md#the-search-filter).

This allows you to craft complex queries using those boolean operators along with parentheses and quotation marks. Surrounding a phrase with quotation marks will search for an exact match of that phrase, after stemming and stop-word removal (be sure to use **double quotation marks** — `"`). Using parentheses will specify order of operations for the boolean operators. Words that are not separated by one of the boolean operators will be interpreted as `AND`.

Behind the scenes, the boolean search is using Elasticsearch's [query string query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) on the searchable fields (such as title, abstract, and fulltext for works; see each individual entity page for specifics about that entity). Wildcard and fuzzy searches using `*`, `?` or `~` are not allowed; these characters will be removed from any searches. These searches, even when using quotation marks, will go through the same cleaning as desscribed above, including stemming and removal of stop words.

* Search for works that mention "elmo" and "sesame street," but not the words "cookie" or "monster": [`https://api.openalex.org/works?search=(elmo AND "sesame street") NOT (cookie OR monster)`](https://api.openalex.org/works?search=%28elmo%20AND%20%22sesame%20street%22%29%20NOT%20%28cookie%20OR%20monster%29)

## Relevance score

When you use search, each returned entity in the results lists gets an extra property called `relevance_score`, and the list is by default sorted in descending order of `relevance_score`. The `relevance_score` is based on text similarity to your search term. It also includes a weighting term for citation counts: more highly-cited entities score higher, all else being equal.

If you search for a multiple-word phrase, the algorithm will treat each word separately, and rank results higher when the words appear close together. If you want to return only results where the exact phrase is used, just enclose your phrase within quotes. Example:

* Get works with the exact phrase "fierce creatures" in the title or abstract (returns just a few results):\
  [`https://api.openalex.org/works?search="fierce%20creatures"`](https://api.openalex.org/works?search=%22fierce%20creatures%22)
* Get works with the words "fierce" and "creatures" in the title or abstract, with works that have the two words close together ranked higher by `relevance_score` (returns way more results):\
  [`https://api.openalex.org/works?search=fierce%20creatures`](https://api.openalex.org/works?search=fierce%20creatures)

## The search filter

You can also use search as a [filter](filter-entity-lists.md), allowing you to fine-tune the fields you're searching over. To do this, you append `.search` to the end of the property you are filtering for:

* Get authors who have "Einstein" as part of their name:\
  [`https://api.openalex.org/authors?filter=display_name.search:einstein`](https://api.openalex.org/authors?filter=display\_name.search:einstein)
* Get works with "cubist" in the title:\
  [`https://api.openalex.org/works?filter=title.search:cubist`](https://api.openalex.org/works?filter=title.search:cubist)

Additionally, the filter `default.search` is available on all entities; this works the same as the [`search` parameter](search-entities.md#the-search-parameter).

{% hint style="info" %}
You might be tempted to use the search filter to power an autocomplete or typeahead. Instead, we recommend you use the [autocomplete endpoint](autocomplete-entities.md), which is much faster.\
\
👎 [`https://api.openalex.org/institutions?filter=display_name.search:florida`](https://api.openalex.org/institutions?filter=display\_name.search:florida)

👍 [`https://api.openalex.org/autocomplete/institutions?q=Florida`](https://api.openalex.org/autocomplete/institutions?q=Florida)
{% endhint %}

# Select fields

You can use `select` to limit the fields that are returned in results.

* Display works with only the `id`, `doi`, and `display_name` returned in the results\
  [`https://api.openalex.org/works?select=id,doi,display\_name`](https://api.openalex.org/works?select=id,doi,display\_name)

```json
"results": [
  {
    "id": "https://openalex.org/W1775749144",
    "doi": "https://doi.org/10.1016/s0021-9258(19)52451-6",
    "display_name": "PROTEIN MEASUREMENT WITH THE FOLIN PHENOL REAGENT"
  },
  {
    "id": "https://openalex.org/W2100837269",
    "doi": "https://doi.org/10.1038/227680a0",
    "display_name": "Cleavage of Structural Proteins during the Assembly of the Head of Bacteriophage T4"
  },
  // more results removed for brevity
]
```

## Limitations

The fields you choose must exist within the entity (of course). You can only select root-level fields.

So if we have a record like so:

```
"id": "https://openalex.org/W2138270253",
"open_access": {
  "is_oa": true,
  "oa_status": "bronze",
  "oa_url": "http://www.pnas.org/content/74/12/5463.full.pdf"
}
```

You can choose to display `id` and `open_access`, but you will get an error if you try to choose `open_access.is_oa`.

You can use select fields when getting lists of entities or a [single entity](../get-single-entities/select-fields.md). It does not work with [group-by](../get-groups-of-entities.md) or [autocomplete](autocomplete-entities.md).&#x20;

# Sort entity lists

Use the `?sort` parameter to specify the property you want your list sorted by. You can sort by these properties, where they exist:

* `display_name`
* `cited_by_count`
* `works_count`
* `publication_date`
* `relevance_score` (only exists if there's a [search filter](sort-entity-lists.md#search) active)

By default, sort direction is ascending. You can reverse this by appending `:desc` to the sort key like `works_count:desc`. You can sort by multiple properties by providing multiple sort keys, separated by commas. Examples:

* All works, sorted by `cited_by_count` (highest counts first)\
  [`https://api.openalex.org/works?sort=cited_by_count:desc`](https://api.openalex.org/works?sort=cited\_by\_count:desc)
* All sources, in alphabetical order by title:\
  [`https://api.openalex.org/sources?sort=display_name`](https://api.openalex.org/sources?sort=display\_name)

You can sort by relevance\_score when searching:

* Sort by year, then by relevance\_score when searching for "bioplastics":\
  [`https://api.openalex.org/works?filter=display_name.search:bioplastics&sort=publication_year:desc,relevance_score:desc`](https://api.openalex.org/works?filter=display\_name.search:bioplastics\&sort=publication\_year:desc,relevance\_score:desc)

An error is thrown if attempting to sort by `relevance_score` without a search query.