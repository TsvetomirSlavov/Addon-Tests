#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.base import Base


class Statistics(Base):

    _title_locator = (By.CSS_SELECTOR, '.addon')
    _total_downloads_locator = (By.CSS_SELECTOR, '.island.two-up div:nth-child(1) a')
    _usage_locator = (By.CSS_SELECTOR, '.island.two-up div:nth-child(2) a')

    @property
    def _page_title(self):
        return "%s :: Statistics Dashboard :: Add-ons for Firefox" % self.addon_name

    @property
    def addon_name(self):
        base = self.selenium.find_element(*self._title_locator).text
        return base.replace('Statistics for', '').strip()

    @property
    def total_downloads_number(self):
        text = self.selenium.find_element(*self._total_downloads_locator).text
        return int(text.split()[0].replace(',', ''))
