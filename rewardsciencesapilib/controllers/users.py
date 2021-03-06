# -*- coding: utf-8 -*-

"""
    rewardsciencesapilib.controllers.users

    This file was automatically generated by APIMATIC BETA v2.0 on 09/13/2016
"""

from .base_controller import *



class Users(BaseController):

    """A Controller to access Endpoints in the rewardsciencesapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def show(self,
                user_id):
        """Does a GET request to /users/{user_id}.

        This endpoint lets retrieve a user's details.

        Args:
            user_id (int): The ID of the user to be retrieved.

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if user_id == None:
            raise ValueError("Required parameter 'user_id' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/users/{user_id}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'user_id': user_id
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'Accept': Configuration.accept,
            'Content-Type': Configuration.content_type,
            'Authorization': 'Bearer ' + Configuration.o_auth_access_token
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body)



    def identify(self,
                 email,
                 first_name = None,
                 last_name = None):
        """Does a POST request to /users.

        This endpoint lets you tie a user with his/her activities. You’ll want
        to identify a user with any relevant information as soon as they
        log-in or sign-up.

        Args:
            email (string): The user's email address
            first_name (string, optional): The user's first name
            last_name (string, optional): The user's last name

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        if email == None:
            raise ValueError("Required parameter 'email' cannot be None.")

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/users'

        # Process optional query parameters
        _query_parameters = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'Accept': Configuration.accept,
            'Content-Type': Configuration.content_type,
            'Authorization': 'Bearer ' + Configuration.o_auth_access_token
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body)


