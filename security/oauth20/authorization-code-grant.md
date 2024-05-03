---
b: https://blendedfeelings.com/software/security/oauth20/authorization-code-grant.md
---

# OAuth 2.0 Authorization Code grant type 
is one of the most common and secure OAuth 2.0 flows. It is designed to work with web applications where the client application (web server) can securely store the client secret. The flow involves several steps and interactions between the client, the authorization server, and the resource owner (user).

Here is how the Authorization Code grant type works:

1. **Authorization Request**: The client directs the resource owner (user) to the authorization server (typically via a browser redirect) with an authorization request. This request includes the client's identity, the requested scope, a redirection URI to which the authorization server will send the user back after granting authorization, and a state parameter to prevent CSRF attacks.

2. **User Authorization**: The user authenticates with the authorization server and decides whether to grant the client application the requested access to their resources.

3. **Authorization Grant**: If the user grants authorization, the authorization server redirects the user back to the client with an authorization code included in the redirect URI. The authorization code is a temporary code that the client will exchange for an access token.

4. **Token Request**: The client makes a request to the authorization server's token endpoint, including the authorization code and the client's credentials (client ID and client secret).

5. **Token Response**: If the authorization server validates the client's credentials and the authorization code, it responds with an access token (and optionally a refresh token). The access token is a string representing the authorization granted to the client.

6. **Accessing Protected Resources**: The client uses the access token to make requests to the resource server for protected resources.

Here's a simplified flow diagram of the Authorization Code grant type:

```
Client (Web App)                Authorization Server                Resource Server
     |                                  |                                  |
     |--(A)- Authorization Request ---->|                                  |
     |                                  |<-(B)-- Authorization Grant ------|
     |                                  |                                  |
     |<-(C)---- Authorization Code ------|                                  |
     |                                  |                                  |
     |--(D)- Access Token Request ----->|                                  |
     |       (with Authorization Code)  |                                  |
     |                                  |                                  |
     |<-(E)------ Access Token ----------|                                  |
     |                                  |                                  |
     |-(F)------ Access Protected Resource ------------------------------->|
     |       (with Access Token)        |                                  |
     |                                  |<-(G)------- Protected Resource ---|
```

- (A) Client initiates the flow by directing the user's browser to the authorization endpoint.
- (B) User authenticates (if not already) and grants permission to the client.
- (C) Authorization server issues an authorization code to the client.
- (D) Client requests an access token from the token endpoint.
- (E) Authorization server issues an access token and optionally a refresh token to the client.
- (F) Client requests the protected resource from the resource server.
- (G) Resource server returns the protected resource to the client.

This flow ensures that the client application never directly handles the user's credentials, and the authorization code is exchanged for an access token in a back-channel communication, which enhances security. The access token can have a limited lifetime, and the client can use a refresh token (if issued) to obtain a new access token without further user interaction when the access token expires.