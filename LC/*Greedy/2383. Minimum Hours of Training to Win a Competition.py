class Solution:
    def minNumberOfHours(self, initialEnergy: int, ie: int, energy: List[int], experience: List[int]) -> int:
        # firstly , I have this solution, but some test cases did not pass
        de = sum(energy) + 1 - initialEnergy
        me = max(experience) + 1
        se = 0
        for i, e in enumerate(experience):
            if e == me:
                se = sum(experience[:i])

        dexp = me - initialExperience - se
        if ie <= experience[0]:
            prac = experience[0] + 1 - ie
            ie += experience[0]
        else:
            prac = 0
            ie += experience[0]

        prac = 0
        for e in range(0, len(experience)):
            pe = ie + sum(experience[:e])

            if pe <= experience[e]:
                prac += experience[e] + 1 - pe

        return prac + de
    # and then, I realized that I could not do this
    # cuz we have to move forward the energy and exp together
    # each position both of them should be 满足


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        en = 0  # Energy
        ex = 0  # Experience

        an = 0  # Added energy
        ax = 0  # Added experience

        for ener, exp in zip(energy, experience):
            if ener >= en:
                an += (ener - en + 1)
                en += (ener - en + 1)
            if exp >= ex:
                ax += (exp - ex + 1)
                ex += (exp - ex + 1)

            en -= ener
            ex += exp

        return max(0, (an - initialEnergy)) + max(0, (ax - initialExperience))