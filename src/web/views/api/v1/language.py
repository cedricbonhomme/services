#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Freshermeat - An open source software directory and release tracker.
# Copyright (C) 2017-2019  Cédric Bonhomme - https://www.cedricbonhomme.org
#
# For more information : https://gitlab.com/cedric/Freshermeat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from bootstrap import manager

from web import models
from web.views.api.v1.common import url_prefix


blueprint_language = manager.create_api_blueprint(
    models.Language,
    url_prefix=url_prefix,
    methods=['GET'])
