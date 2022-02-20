import urllib.error as ue
import urllib.request as ur

class InternetChecker:
    '''
        Identifies the internet status of the user. Prompts the user to use the provided local database if their
        internet latency is too high.
    '''
    def internet_latency_check(self) -> bool:
        '''
            Attempts to access google.com with an one second timeout theshold.
            :rtype: bool
        '''
        try:
            s = ur.urlopen("http://www.google.com", timeout=1)
            return True
        except ue.URLError as ex:
            return False

if __name__ == "__main__":
    ic = InternetChecker()
    print(ic.internet_latency_check())