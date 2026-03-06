
public class KD2 {
    String player;
    double kills;
    double deaths;
    double kd;

    public KD2(String player, int kills, int deaths){
        this.player = player;
        this.kills = kills;
        this.deaths = deaths;
        this.kd = (double) kills / deaths;
    }
}

