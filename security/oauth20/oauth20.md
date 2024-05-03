---
b: https://blendedfeelings.com/software/security/oauth20/oauth20.md
---

# OAuth 2.0 
is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites without giving them the passwords. It provides to clients a "secure delegated access" to server resources on behalf of a resource owner. It specifies a process for resource owners to authorize third-party access to their server resources without sharing their credentials.

Here is an overview of the main components in OAuth 2.0:

1. **Resource Owner**: Typically, this is the end-user who owns the data or has the rights to access the protected resources.

2. **Resource Server**: This is the server hosting the protected resources. It is capable of accepting and responding to protected resource requests using access tokens.

3. **Client**: The application or system that wants to access the resource owner's data. The client must be authorized by the resource owner to access the protected resource.

4. **Authorization Server**: This is the server that authenticates the resource owner and issues access tokens to the client after getting proper authorization.

The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.

OAuth 2.0 defines four grant types:

1. **Authorization Code**: Used by Web Apps executing on a server. This is the most common type and considered the most secure.

2. **Implicit**: Was previously recommended for clients without a secret, but is now considered insecure and should be avoided.

3. **Resource Owner Password Credentials**: Should only be used when there is a high degree of trust between the resource owner and the client (e.g., the client is part of the device's operating system).

4. **Client Credentials**: Used for applications API access.

The OAuth 2.0 process generally follows these steps:

1. The client requests authorization from the resource owner to access the protected resources.
2. If the resource owner grants authorization, the client uses the authorization grant to request an access token from the authorization server.
3. The authorization server authenticates the client and the resource owner, validates the authorization grant, and if valid, issues an access token.
4. The client requests the protected resource from the resource server and authenticates by presenting the access token.
5. If the access token is valid, the resource server serves the request.

OAuth 2.0 is widely used in the industry and serves as the foundation for other protocols, such as OpenID Connect, which is built on top of OAuth 2.0 and provides identity layer functionalities.