import requests
import sys
import json
import argparse


class EmailError(Exception):
    def __init__(self, message=None):
        super(EmailError, self).__init__(message)


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Checks if an e-mail address exists or not ')

    parser.add_argument(
        'email',
        metavar='EMAIL',
        type=str,
        help='e-mail to check')

    return parser.parse_args()


def google_mail(email):
    data = {'Email': email}
    response = requests.post('https://accounts.google.com/_/signin/v1/lookup', data=data)
    text = json.loads(response.text)
    is_valid = text['action'] == 'ASK_PASSWORD'
    return is_valid


def yahoo_mail(email):
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'B=5n2a91dcpt6q6&b=3&s=hl; DNT=1; AS=v=1&s=weJ4rtnY&d=A599e9f0d|4MfQbfr.2QK51RTfRTeNYb4_T114PiA.freiWhiRpxMv9zLkIlneUhtO21jiBHWAmwYHv9cvtLqvkNCVBA6ICS6tQiV880aWZ8egRKvJU4AW69X6WuLQEfi4VVN0Uv0FR4alI6CfukGZ56_1WOHiOdXEjZ7MUfT.RpM8ZFAlBcDFgUjNkowBRceEbkVzuwnd5o23aC7kl9XBB.GORce2ZMLwftNUhO0wU3lgXd7uos3ec5urnIqzuIhtSBUg9LqwoulRcnfYpXhGNBqkCqgzB_bpGjV0HcLPs8aPitTjAGfq2.kkxeixDBh7w2VLn5_VfhZ0w0RGCROXZUl1TVCIo5x9KB3VkVAc3u5SzHdsU9WdW2kF11mvocLd2TKp_b0D7QmFEvo6k.CZmDUjH6Fs.QUDtniVTBLFaN6Tz.riLg8U8CoQu4fOfTq7qIbo8Cperbd3ZOX.xYauthIpBVYmCub_mLHGOYjFazGH0WWwH3Vs.yi70F7uRur_Z.v3UX70nOjfmAmENpK7nK7fbFOkmqmZQUkJB6UiMiCSKq6WTrh.TxWukt9wTZRaW7gC1uOPyvIOHO.f_69lT9wcETPc7CgRg4qPk2DzusHLe_dta18hIXDXsbpF1lZbrJ1pIQA8zygPcZF2Cxr5DpiwHVQ5hxGj1HeSeMwBp5Nkci2DLHcnii3yf8HQ9HeaV9i4c4ULA3t7K7INcQqpi4jDndRl7fp21oAFH6h5FqRNRw2uLaqgEGrO.a0QSNfwCWf5g7kDqQdlVkwVQBAbHQmwxTQTgIu.5iRIb.oahFrZ9p8CwcS7RG9QZLNudr9pAEYkuljuzTTagE7QRq8Oj7DPTsWyknuA4mtxpa3130a25rCBWLO8_ISxIU9JcNl9E9sHUjPwVQ--~A|B599fed7a|Wdwbgxv.2cLWbhmkl07xv9v_rRYvVlGibiv5NfxqSv1Uz3KcYtl_S1TK4IsTwL8PAsljLhVocMdpAkouEIJKRJ4rCzEBgcnAPUka5W6er7vGA0hg8Zl4fRm9PQztJFHMuuwdiMfvX_LI_MC8k59kwtcxblZLoYNv5UXgL0d73Iw8qa4_193dIhEUrWgrh1RQk5sPki2nBk62XDFFBP8U.cfGEMQTyiu8gYP9nHFV3e_dp9537E3CeAUlJv0UmrIusV8D83hIvDNi9sOg1lTuLmXLD_KRhLBzK30zu4ejb_eY4U.dU.izQS1Bqf3ADGcp.cLujv5nhcQlzILSStxUoBSn4RhSYEIrcmg_Fxfq55gjz9iRSlF.BIIAKS7A.OfWA_zmP3oc0uH0wJ.BhQ3rS2LsWSr0TzJ8cu5ydbb_5YRYmlg3aUCMsmZojFUYzh.MINUbZIDiXtWGMEZY8LtjlhRWaoPnrAD4Mk6uCuviISjVuMn5GnTO6RHKxnMBV4tHUuhLWwEg9q_PtBhDPMk9ST0R4kzWJ8e3ScP7.Q5hfSaBdtvQu2VsbRiAloxUnOKk8WlC1p22WSasndvebe0ostgTuw5vzO7_Y437wNLQAROl8X62pYY20fPca9KHN1U-~A',
    }

    data = {
        'username': email,
        'acrumb': 'weJ4rtnY',
        'config': 'CA2JQzH.2bL13DGK0Wdlytfoj1r.QXP6E2VTbblQ2_CC0B3HcPrWbMjmFgkFQhsHYPS0C.ss_pDqnqAJuHKRtDci854SksJf_2.0nyF7s6u5unZvKkwFwnlG3qm2cmpHsxKBMonv64FvmTlDgkJ8uSHP672HlTcQtOETmoQ3S0cERY0LX1baqB63efVh8qXzt8x7Bw2iRCeQP49l1vPN7Fnfy5nlmO18mywFo_BIj3NxNm4qINov~A',
        'session': 'Qg--',
    }

    response = requests.post('https://login.yahoo.com/config/login?', headers=headers, data=data)
    text = json.loads(response.text)
    is_valid = 'error' in text
    return is_valid


def validate(email):
    if email.endswith('@gmail.com'):
        is_valid = google_mail(email)
    elif email.endswith('@yahoo.com'):
        is_valid = yahoo_mail(email)
    else:
        raise EmailError('This e-mail service is not supported currently. Please submit an issue on https://github.com/ritiek/email-validator/issues and thank you!')
    return is_valid


def command_line():
    args = get_arguments()
    email = args.email

    try:
        is_valid = validate(email)

        if is_valid:
            result = email + ' is a valid e-mail address'
        else:
            result = email + ' is not a valid e-mail address'

        print(result)

    except EmailError:
        print('This e-mail service is not supported currently. Please submit an issue on https://github.com/ritiek/email-validator/issues and thank you!')


if __name__ == '__main__':

        command_line()
