---
b: https://blendedfeelings.com/software/security/oauth20/implicit-grant.md
---

# OAuth 2.0 Implicit Grant 
is a simplified authorization flow that was originally designed for client-side web applications, such as those written in JavaScript and running in a user's web browser. This flow allows the application to obtain an access token from the authorization server without the need for any server-side components.

Here's a general outline of how the Implicit Grant flow works:

1. **Client Registration**: Before starting the OAuth flow, the client application must be registered with the authorization server. This registration typically involves specifying a redirect URI to which the server will send the access token.

2. **Authorization Request**: The client application redirects the user's browser to the authorization server with a request for access. This request includes the client ID, response type (`token`), redirect URI, scope, and possibly a state parameter to mitigate CSRF attacks.

3. **User Authentication and Consent**: The authorization server authenticates the user (usually through a login form) and asks for their consent to grant access to their data for the scopes requested by the application.

4. **Access Token Issued**: If the user grants consent, the authorization server redirects the user-agent back to the client application with the access token included in the fragment part of the redirect URI.

5. **Client Retrieves Token**: The client application can now extract the access token from the URI fragment using JavaScript.

6. **Access Protected Resources**: The client application can use the access token to make requests to the resource server on behalf of the authenticated user.

The Implicit Grant flow was considered less secure than other OAuth 2.0 flows because the access token is exposed in the URL fragment and can be accessed by any JavaScript running in the browser. Due to these security concerns, the OAuth 2.0 Security Best Current Practice document recommends against using the Implicit Grant flow and suggests using the Authorization Code Grant with PKCE (Proof Key for Code Exchange) instead, especially for new applications.

As of my last update, the Implicit Grant is still part of the OAuth 2.0 specification, but developers are encouraged to migrate to more secure flows for their applications.