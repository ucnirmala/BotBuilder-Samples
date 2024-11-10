i#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

# Added to support interaction with Azure AI Language API
    ENDPOINT_URI = os.environ.get("MicrosoftAIServiceEndpoint","")
    print(f"ENDPOINT_URI = {ENDPOINT_URI}")
    API_KEY = "31QYkliaFjVnWaKCw6HpE0qepE9fUN2MOXPIGC4RXi6S2LIYw6LbJQQJ99AKACYeBjFXJ3w3AAAaACOGPTlU"
