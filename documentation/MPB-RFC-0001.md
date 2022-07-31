# MPB-RFC-0001

---

*Disclaimer*: The MPB-RFCs define the protocols of communication between components within the MPB project. Their purpose is to be a localized standard, and their usage outside of the scope of this project is offered AS-IS with no warranty or guarantees.

---

*Glossary*: To fully statisfy the defined protocol the implementation MUST and MUST NOT do as indicated. To follow recommendations the implementation SHOULD or SHOULD NOT do as suggested.

---

## Definition

The MPB-RFC-0001 indicates the interface the MPB services MUST satisfy to be fully an MPB service.

A service MUST provide an `HTTP/1.1` or `HTTP/2` server, that SHOULD be `HTTP/2`, and MUST provide a non `HTTP 5xx` response for the root domain in EVERY method. Non supported methods MUST return an `HTTP 405` with necessary headers [RFC 7231, Sec. 6.5.5.](https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.5).

## Details

:warning: under construction :warning: