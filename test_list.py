import pickle


def test_list():
    with open('./data/pickled_lists/total_links_list.pkl', 'rb') as fp:
        links = pickle.load(fp)
    assert all(isinstance(s, str) for s in links)