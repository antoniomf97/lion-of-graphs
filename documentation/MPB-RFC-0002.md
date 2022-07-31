# MPB-RFC-0002

---

*Disclaimer*: The MPB-RFCs define the protocols of communication between components within the MPB project. Their purpose is to be a localized standard, and their usage outside of the scope of this project is offered AS-IS with no warranty or guarantees.

---

*Glossary*: To fully statisfy the defined protocol the implementation MUST and MUST NOT do as indicated. To follow recommendations the implementation SHOULD or SHOULD NOT do as suggested.

---

## Definition

The MPB-RFC-0002 indicates the interface a MPB plotter service MUST provide to be used with the current MPB application.

The plotter service MUST satisfy the previous [MPB-RFC-0001](./MPB-RFC-0001.md) and MUST provide `OPTIONS` and `POST` methods at the root level. The `OPTIONS` will dictate the server available communication options and the `POST` request MUST be able to take a file (e.g., `csv`) to process and return an appropriate drawing response as described in the details section of this document.

## Details

### / OPTIONS

The plotter `OPTIONS` method MUST provide a response with the allowed headers, (...) [RFC 7231, Sec. 4.3.7.](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.7)

:warning: under construction :warning:

### / POST

The plotter `POST` method MUST be able to accept a request with a file (e.g., `csv`) in the form of a `multipart/form-data` as described in [RFC2388](https://datatracker.ietf.org/doc/html/rfc2388) with the key `file`, file type and rules in the key `filetype`, and plot dimensions in the key `dimensions`. The processing SHOULD take into consideration the given data and dimensions and MUST return a successful response with an `application/json` with two keys, a `graphtype` which can either be `points` or `paths` and a list of, respectively, points or [paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d).

The input file SHOULD be within (...)

If the plotter service is not able to process or does not recognize the `filetype` it MUST answer with an `HTTP 400` with a valid explanation of the source of error.

---

Examples

---

Successful request

POST REQUEST
```
> POST / HTTP/1.1
> Host: example.com
> User-Agent: example/agent
> Content-Length: N
> Content-Type: multipart/form-data

(...)
```

POST RESPONSE
```
< HTTP/1.1 200 OK
< Content-Type: application/json
< Server: example.server
< Content-Length: N
{
    "graphtype": "points",
    "points": [{"x": 10, "y": 10}, {"x": 100, "y": 20}, {"x": 200, "y": 300}, {"x": 10, "y": 10}]
}
```

:warning: under construction :warning:
