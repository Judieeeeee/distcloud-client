# Copyright (c) 2017 Ericsson AB.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Copyright (c) 2020-2021 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use
# of this software may be licensed only pursuant to the terms
# of an applicable Wind River license agreement.
#
from dcmanagerclient.api.v1.sw_update_manager import sw_update_manager

SW_UPDATE_TYPE_KUBERNETES = "kubernetes"


class kube_upgrade_manager(sw_update_manager):

    def __init__(self, http_client):
        super(kube_upgrade_manager, self).__init__(
            http_client,
            update_type=SW_UPDATE_TYPE_KUBERNETES)
